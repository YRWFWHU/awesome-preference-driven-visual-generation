#!/usr/bin/env python3
"""Validate the curated catalog and local links offline using only Python's standard library."""
from datetime import date
from difflib import SequenceMatcher
import json
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import urlsplit, unquote

ROOT=Path(__file__).resolve().parents[1]
REQUIRED_FILES=['README.md','LICENSE','CONTRIBUTING.md','references.bib','data/resources.json',
 'docs/research-guide.zh-CN.md','docs/scope-and-taxonomy.md','docs/search-backlog.md',
 'scripts/build.py','scripts/validate.py','.github/workflows/validate.yml',
 '.github/ISSUE_TEMPLATE/add-resource.yml','.github/pull_request_template.md','.gitignore']
STATES={'yes','no','unclear','not_applicable'}
ENUMS={
 'resource_type':{'paper','dataset','benchmark','tool','survey'},
 'scope':{'core','supporting','adjacent'},
 'category':{'history-conditioned-generation','user-conditioned-generation','interactive-preference-generation',
 'personalized-reward-guided-generation','personalized-generation-benchmark','personalized-aesthetic-assessment',
 'user-level-preference-data','personalized-preference-model','population-preference-alignment','cohort-conditioned-generation','style-customization','subject-customization'},
 'user_data_origin':{'real','synthetic','mixed','unclear','not_applicable'},
 'new_user_optimization':STATES,'evaluates_unseen_users':STATES,'evaluates_new_prompts':STATES,'used_for_generation':STATES,
 'code_status':{'available','partial','announced','inaccessible','not_found','unverified','not_applicable'},
 'publication_status':{'preprint','submitted','accepted','published','withdrawn','unknown'}
}
TAGS={
 'tasks':{'generation','editing','preference_prediction','evaluation'},
 'user_signals':{'likes','likes_dislikes','ratings','pairwise','natural_language','implicit_history','reference_target','rankings'},
 'methods':{'prompt_rewriting','user_representation','adapter_fine_tuning','reward_guidance','retrieval_in_context','active_elicitation'},
 'evaluation':{'target_user_study','third_party_human','personalized_scorer','generic_reward','similarity_proxy','llm_judge','simulation','held_out_user_ratings','online_engagement'}
}
SOURCE_KINDS={'paper','proceedings','conference_decision','author_project','official_repository','dataset_card','model_card','publisher_metadata'}
BASE_REQUIRED=['id','title','resource_type','scope','category','summary','inclusion_reason','primary_url','sources','verified_on',
 'tasks','user_signals','methods','user_data_origin','new_user_optimization','evaluates_unseen_users','evaluates_new_prompts',
 'evaluation','base_models','used_for_generation','evidence_note','limitations','conflicts','related_ids','code_status','code_note','dataset_details']
PAPER_REQUIRED=['authors','first_publication_date','first_publication_date_note','publication_year','venue','publication_status',
 'arxiv_id','doi','official_code_url','project_url','bibtex']
URL_FIELDS={'primary_url','official_code_url','project_url','data_url','model_url','url','source_url'}


def is_url(value):
    if not isinstance(value,str) or re.search(r'[\s<>]',value):return False
    try:
        p=urlsplit(value)
        return p.scheme in {'http','https'} and bool(p.hostname) and not p.username and not p.password and (p.port is None or 0<p.port<65536)
    except ValueError:return False


def valid_date(value,partial=False):
    if not isinstance(value,str):return False
    if partial and re.fullmatch(r'\d{4}',value):return 1<=int(value)<=9999
    if partial and re.fullmatch(r'\d{4}-\d{2}',value):value+='-01'
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',value):return False
    try:date.fromisoformat(value);return True
    except ValueError:return False


def normalized_title(value):
    return re.sub(r'[^\w]','',unicodedata.normalize('NFKC',value).casefold())


def validate_data(data,today=None):
    today=today or date.today();errors=[];warnings=[]
    def err(path,msg):errors.append(f'{path}: {msg}')
    if not isinstance(data,dict) or type(data.get('schema_version')) is not int or data.get('schema_version')!=1 or not isinstance(data.get('resources'),list):
        return ['Root must be an object with schema_version=1 and a resources array.'],warnings
    if not data['resources']:err('resources','must not be empty')
    seen={};arxiv_seen={};doi_seen={};bib_seen={};papers=[]
    for index,r in enumerate(data['resources']):
        path=f'resources[{index}]'
        if not isinstance(r,dict):err(path,'must be an object');continue
        required=BASE_REQUIRED+(PAPER_REQUIRED if r.get('resource_type')=='paper' else [])
        for key in required:
            if key not in r:err(path,f'missing {key}')
        rid=r.get('id')
        if not isinstance(rid,str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',rid):err(path,'invalid stable id')
        elif rid in seen:err(path,'duplicate id '+rid)
        else:seen[rid]=r
        for k in ['title','summary','inclusion_reason','primary_url','evidence_note','limitations','code_note']:
            if not isinstance(r.get(k),str) or not r[k].strip():err(path,k+' must be a nonempty string')
        for k,allowed in ENUMS.items():
            if k in r and (not isinstance(r[k],str) or r[k] not in allowed):err(path,'invalid '+k)
        for k,allowed in TAGS.items():
            v=r.get(k)
            if not isinstance(v,list) or any(not isinstance(x,str) or x not in allowed for x in v):err(path,'invalid '+k+' array')
            elif len(v)!=len(set(v)):err(path,'duplicate '+k+' tags')
        for k in ['base_models','conflicts','related_ids']:
            if k=='base_models' and r.get(k) is None:continue
            if not isinstance(r.get(k),list) or any(not isinstance(x,str) or not x.strip() for x in r.get(k,[])):err(path,'invalid '+k+' array')
        verified=r.get('verified_on')
        if not valid_date(verified):err(path,'invalid verified_on date')
        elif date.fromisoformat(verified)>today:err(path,'verified_on is in the future')
        sources=r.get('sources')
        if not isinstance(sources,list) or not sources:err(path,'at least one checked primary source required');sources=[]
        checked=[]
        for s in sources:
            if not isinstance(s,dict):err(path,'source must be an object');continue
            if not is_url(s.get('url')):err(path,'invalid source URL')
            if not isinstance(s.get('kind'),str) or s['kind'] not in SOURCE_KINDS:err(path,'invalid source kind')
            if not isinstance(s.get('note'),str) or not s['note'].strip():err(path,'source note required')
            d=s.get('checked_on')
            if not valid_date(d):err(path,'invalid source checked_on')
            elif date.fromisoformat(d)>today:err(path,'source check is in the future')
            else:checked.append(d)
        if checked and valid_date(verified) and max(checked)!=verified:err(path,'verified_on must equal latest recorded source check')
        def walk_urls(obj):
            if isinstance(obj,dict):
                for k,v in obj.items():
                    if k in URL_FIELDS and v is not None and not is_url(v):err(path,'invalid URL in '+k)
                    walk_urls(v)
            elif isinstance(obj,list):
                for x in obj:walk_urls(x)
        walk_urls(r)
        if isinstance(r.get('code_status'),str) and r['code_status'] in {'available','partial','inaccessible'} and not r.get('official_code_url'):err(path,'code status needs official_code_url')
        if r.get('scope')=='core' and r.get('used_for_generation')!='yes':err(path,'core method must demonstrate generation/editing')
        d=r.get('dataset_details')
        if d is not None:
            if not isinstance(d,dict):err(path,'dataset_details must be null or object')
            else:
                if not isinstance(d.get('origin'),str) or d['origin'] not in ENUMS['user_data_origin']:err(path,'invalid dataset_details.origin')
                for k in ['name','user_identity','feedback','size_note','evaluation_note']:
                    if not isinstance(d.get(k),str) or not d[k].strip():err(path,'dataset_details.'+k+' required')
        if 'reading_order' in r:
            if type(r['reading_order']) is not int or r['reading_order']<1:err(path,'reading_order must be a positive integer')
            if not isinstance(r.get('reading_reason'),str) or not r['reading_reason'].strip():err(path,'reading_reason required')
        if r.get('resource_type')=='paper':
            if r.get('venue') is not None and not isinstance(r['venue'],str):err(path,'venue must be a string or null')
            if not isinstance(r.get('first_publication_date_note'),str) or not r['first_publication_date_note'].strip():err(path,'first publication provenance required')
            a=r.get('authors')
            if not isinstance(a,list) or not a or any(not isinstance(x,str) or not x.strip() for x in a):err(path,'ordered author names required')
            first=r.get('first_publication_date')
            if first is not None and not valid_date(first,True):err(path,'invalid first_publication_date precision')
            elif first and first>today.isoformat():err(path,'first publication is in the future')
            y=r.get('publication_year')
            if y is not None and (type(y) is not int or not 1000<=y<=today.year):err(path,'invalid publication_year')
            if isinstance(r.get('publication_status'),str) and r['publication_status'] in {'published','accepted'}:
                if not isinstance(r.get('venue'),str) or not r['venue'].strip():err(path,'verified venue required')
                if not any(isinstance(s,dict) and isinstance(s.get('kind'),str) and s['kind'] in {'proceedings','conference_decision','publisher_metadata'} for s in sources):err(path,'publication/acceptance requires official source')
            arxiv=r.get('arxiv_id')
            if arxiv is not None:
                if not isinstance(arxiv,str) or not re.fullmatch(r'(?:\d{4}\.\d{4,5}|[a-z.-]+/\d{7})(?:v\d+)?',arxiv):err(path,'invalid arxiv_id')
                else:
                    canonical=re.sub(r'v\d+$','',arxiv).lower()
                    if canonical in arxiv_seen:err(path,'duplicate arXiv ID with '+arxiv_seen[canonical])
                    arxiv_seen[canonical]=str(rid)
            doi=r.get('doi')
            if doi is not None:
                if not isinstance(doi,str) or not re.fullmatch(r'10\.\d{4,9}/\S+',doi):err(path,'invalid DOI (use bare DOI)')
                else:
                    canonical=doi.casefold()
                    if canonical in doi_seen:err(path,'duplicate DOI with '+doi_seen[canonical])
                    doi_seen[canonical]=str(rid)
            b=r.get('bibtex')
            if b is not None:
                if not isinstance(b,dict):err(path,'bibtex must be null or object')
                else:
                    key=b.get('key')
                    if not isinstance(key,str) or not re.fullmatch(r'[A-Za-z][A-Za-z0-9:_-]*',key):err(path,'invalid BibTeX key')
                    elif key in bib_seen:err(path,'duplicate BibTeX key '+key)
                    else:bib_seen[key]=rid
                    if not isinstance(b.get('entry_type'),str) or b['entry_type'] not in {'article','inproceedings','misc'}:err(path,'invalid BibTeX entry_type')
                    for field in ['container','pages']:
                        if b.get(field) is not None and not isinstance(b[field],str):err(path,'invalid BibTeX '+field)
                    if y is None or not a:err(path,'BibTeX needs verified authors and year')
                    if not is_url(b.get('source_url')):err(path,'BibTeX provenance required')
                    if b.get('source_url') not in [s.get('url') for s in sources if isinstance(s,dict)]:err(path,'BibTeX provenance must be a checked source')
            if isinstance(r.get('title'),str):papers.append((str(rid),normalized_title(r['title'])))
    for rid,r in seen.items():
        related=r.get('related_ids')
        if isinstance(related,list):
            for other in related:
                if not isinstance(other,str) or other not in seen:err(rid,'invalid related_id '+str(other))
                elif other==rid:err(rid,'self-referential related_id')
    for i,(rid,title) in enumerate(papers):
        for other,otitle in papers[i+1:]:
            if title==otitle:err(rid,'duplicate normalized paper title with '+other)
            elif SequenceMatcher(None,title,otitle).ratio()>.90:warnings.append(f'{rid}: similar paper title to {other}; review for duplication')
    return errors,warnings


def anchors(text):
    values=set(re.findall(r'<a\s+id=[\"\']([^\"\']+)',text))
    occurrences={}
    for heading in re.findall(r'^#{1,6}\s+(.+)$',text,re.M):
        h=re.sub(r'[`*_]','',heading.strip()).lower()
        h=re.sub(r'[^\w\- ]','',h).replace(' ','-')
        n=occurrences.get(h,0);occurrences[h]=n+1
        values.add(h+(f'-{n}' if n else ''))
    return values


def validate_files(root=ROOT):
    errors=[]
    for name in REQUIRED_FILES:
        if not (root/name).is_file():errors.append('Missing required file: '+name)
    for path in root.rglob('*.md'):
        if '.git' in path.parts:continue
        text=path.read_text(encoding='utf-8')
        text=re.sub(r'```.*?```','',text,flags=re.S)
        for raw in re.findall(r'\[[^\]]*\]\(([^\n]+?)\)',text):
            target=raw.strip().strip('<>')
            if target.startswith(('http:','https:')):
                if not is_url(target):errors.append(f'{path.relative_to(root)}: malformed URL {target}')
                continue
            parsed=urlsplit(target)
            if parsed.scheme or parsed.netloc:
                errors.append(f'{path.relative_to(root)}: unsupported link {target}');continue
            destination=(path.parent/unquote(parsed.path)).resolve() if parsed.path else path
            if not destination.is_relative_to(root.resolve()) or not destination.exists():
                errors.append(f'{path.relative_to(root)}: broken or escaping relative link {target}');continue
            if parsed.fragment and destination.suffix=='.md':
                if unquote(parsed.fragment) not in anchors(destination.read_text(encoding='utf-8')):
                    errors.append(f'{path.relative_to(root)}: missing anchor {target}')
    bib=root/'references.bib'
    if bib.exists():
        keys=re.findall(r'^@\w+\s*\{\s*([^,\s]+)',bib.read_text(encoding='utf-8'),re.M)
        if len(keys)!=len(set(keys)):errors.append('Duplicate BibTeX key in references.bib')
    return errors


def main():
    try:data=json.loads((ROOT/'data/resources.json').read_text(encoding='utf-8'))
    except (OSError,ValueError) as exc:print('ERROR: '+str(exc));return 1
    errors,warnings=validate_data(data)
    errors+=validate_files()
    for message in warnings:print('WARNING: '+message)
    for message in errors:print('ERROR: '+message)
    if errors:return 1
    print(f"Validated {len(data['resources'])} records and local files offline ({len(warnings)} warnings). External availability was not tested.")
    return 0

if __name__=='__main__':sys.exit(main())
