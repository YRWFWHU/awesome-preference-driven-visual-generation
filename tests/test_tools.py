"""Regression tests for the publication maintenance contract; no external requests."""
import copy
from datetime import date, timedelta
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import build
import validate


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads((ROOT/'data/resources.json').read_text())

    def test_current_catalog(self):
        self.assertEqual(validate.validate_data(self.data)[0],[])

    def test_wrong_root_type(self):
        for value in [[],None,{'schema_version':True,'resources':[]}]:
            self.assertTrue(validate.validate_data(value)[0])

    def test_future_dates_and_invalid_precision(self):
        r=self.data['resources'][0]
        r['verified_on']=(date.today()+timedelta(days=1)).isoformat()
        r['first_publication_date']='2025-02-30'
        errors=validate.validate_data(self.data)[0]
        self.assertTrue(any('future' in e for e in errors))
        self.assertTrue(any('first_publication_date' in e for e in errors))
        self.assertTrue(validate.valid_date('2024-02',True))
        self.assertFalse(validate.valid_date('2024-13',True))

    def test_versioned_arxiv_and_case_insensitive_doi(self):
        a,b=self.data['resources'][:2]
        b['arxiv_id']=a['arxiv_id']+'v2'
        a['doi']='10.1234/Test';b['doi']='10.1234/test'
        errors=validate.validate_data(self.data)[0]
        self.assertTrue(any('duplicate arXiv' in e for e in errors))
        self.assertTrue(any('duplicate DOI' in e for e in errors))

    def test_ids_relations_and_bibkeys(self):
        a,b=self.data['resources'][:2]
        b['id']=a['id'];b['bibtex']['key']=a['bibtex']['key'];a['related_ids']=['missing-id']
        errors=validate.validate_data(self.data)[0]
        for term in ['duplicate id','duplicate BibTeX','invalid related_id']:
            self.assertTrue(any(term in e for e in errors),term)

    def test_missing_sources_and_invalid_types(self):
        for field,value in [('sources',[]),('authors','Someone'),('methods','fine_tuning'),('publication_status',[]),('code_status',[])]:
            d=copy.deepcopy(self.data);d['resources'][0][field]=value
            self.assertTrue(validate.validate_data(d)[0],field)
        d=copy.deepcopy(self.data);d['resources'][0]['sources'][0]['kind']=[]
        self.assertTrue(validate.validate_data(d)[0])
        d['resources'][0]['bibtex']['entry_type']=[]
        self.assertTrue(validate.validate_data(d)[0])

    def test_near_titles_warn_without_false_exact_duplicate(self):
        a,b=self.data['resources'][:2]
        b['title']=a['title']+' II'
        errors,warnings=validate.validate_data(self.data)
        self.assertTrue(warnings)
        self.assertFalse(any('normalized paper title' in e for e in errors))

    def test_bad_url(self):
        self.data['resources'][0]['primary_url']='https://'
        self.assertTrue(validate.validate_data(self.data)[0])
        self.assertFalse(validate.is_url('https://example.org:bad'))


class BuildAndFilesTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)/'repo'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__'))

    def run_build(self,*args):
        return subprocess.run([sys.executable,str(self.root/'scripts/build.py'),*args],capture_output=True,text=True)

    def test_check_is_read_only_on_stale_outputs(self):
        bib=self.root/'references.bib';bib.write_text('stale\n')
        result=self.run_build('--check')
        self.assertNotEqual(result.returncode,0)
        self.assertEqual(bib.read_text(),'stale\n')

    def test_build_preserves_manual_text_and_is_deterministic(self):
        path=self.root/'README.md';original=path.read_text()
        original='Custom manual preface.\n'+original+'\nCustom manual suffix.\n';path.write_text(original)
        self.assertEqual(self.run_build().returncode,0)
        generated=path.read_text()
        self.assertEqual(generated.split(build.START)[0],original.split(build.START)[0])
        self.assertEqual(generated.split(build.END)[1],original.split(build.END)[1])
        self.assertEqual(self.run_build().returncode,0)
        self.assertEqual(path.read_text(),generated)
        self.assertEqual(self.run_build('--check').returncode,0)

    def test_bad_markers_do_not_overwrite(self):
        path=self.root/'README.md';original=path.read_text().replace(build.END,'')
        path.write_text(original)
        self.assertNotEqual(self.run_build().returncode,0)
        self.assertEqual(path.read_text(),original)

    def test_local_links_and_bib_duplicates(self):
        p=self.root/'docs/research-guide.zh-CN.md'
        p.write_text(p.read_text()+'\n[missing](missing.md)\n[anchor](../README.md#missing-anchor)\n')
        b=self.root/'references.bib';b.write_text(b.read_text()+'\n@misc{ppd, title={duplicate}}\n')
        errors=validate.validate_files(self.root)
        for term in ['relative link','missing anchor','Duplicate BibTeX']:
            self.assertTrue(any(term in e for e in errors),term)


if __name__=='__main__':unittest.main()
