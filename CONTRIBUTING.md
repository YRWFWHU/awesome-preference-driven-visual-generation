# Contributing

Contributions should improve coverage or evidence quality, not maximize the number of links. Read the [scope policy](docs/scope-and-taxonomy.md) first. All original contributions are dedicated under [CC0-1.0](LICENSE); linked resources retain their own licenses. Do not upload private histories, unpublished proposals, downloaded papers or model/data assets.

## Add or update a resource

1. Identify the individual-user signal and the demonstrated task. Explain why the record is core, supporting or adjacent; keep ambiguous candidates in [the backlog](docs/search-backlog.md).
2. Read primary sources: original paper, publisher/proceedings, official decision, author project and author-linked resources. Search snippets and another bibliography can suggest candidates but cannot verify key claims. Confirm ordered authors, full title and dates from the source itself.
3. Check arXiv ID, DOI and title against existing records. Merge preprint and proceedings versions. Resolve acronym collisions with different stable IDs. Record title/status/data conflicts explicitly.
4. Edit **only [data/resources.json](data/resources.json)** for structured metadata. Do not manually edit the generated README region or references.bib. For a separately useful dataset or tool, link to its parent through `related_ids`; it will not count as an extra paper.
5. Supply actual source-check dates and short evidence notes pointing to sections/tables. Distinguish predicted ratings, generation results, target-user judgments, third-party judgments and model proxies. For reported improvements use “the paper reports”; never claim independent reproduction without one.
6. Run the commands below. Inspect the generated diff, including counts, BibTeX, reading route and resource availability labels. Update manual guidance only when needed.

```bash
python scripts/build.py
python scripts/validate.py
python scripts/build.py --check
python -m unittest discover -s tests
```

Python 3.10+ and the standard library are sufficient. `python3` is equivalent on systems without a `python` alias. Run from the repository root; the scripts also resolve data relative to their own location. CI does not use an external link checker.

## Schema version 1

The root object contains `schema_version: 1` and a `resources` array. The executable schema is in [scripts/validate.py](scripts/validate.py); no second metadata database exists. Text fields are original concise prose in English. IDs and enum values are case-sensitive. Add tags/categories deliberately in the validator and this guide when a new concept is needed.

| Fields | Type / rule |
| --- | --- |
| `id`, `title`, `summary`, `inclusion_reason` | Required nonempty strings; ID is stable lowercase letters/digits separated by hyphens. Title is the verified canonical title, not an inferred expansion of an acronym. |
| `resource_type` | `paper`, `dataset`, `benchmark`, `tool`, `survey`. Papers introducing datasets still use `paper`; an independently listed released asset uses its own resource type. |
| `scope` | `core`, `supporting`, `adjacent`. No core count inflation from adjacent methods. |
| `category` | One navigation category from the list below; does not replace multi-label mechanisms. |
| `primary_url` | Required HTTP(S) paper/resource landing URL. |
| `sources` | Nonempty array of `{url, kind, checked_on, note}`. `note` says what was checked and, where useful, a section/table or access limitation. |
| `verified_on` | `YYYY-MM-DD`, latest actual recorded source check. Every source keeps its own date; never update all dates just by rebuilding. Dates in the initial pass use UTC. |
| `tasks`, `user_signals`, `methods`, `evaluation` | Arrays of controlled tags below; combinations are allowed. No inferred human study just because the dataset contains real users. |
| `user_data_origin` | `real`, `synthetic`, `mixed`, `unclear`, `not_applicable`; describes preference-bearing data, not whether images are photographs or generated. Detail synthetic training versus real evaluation in the evidence note. |
| `new_user_optimization` | `yes`, `no`, `unclear`, `not_applicable`. Concerns new-user parameter optimization (including user embeddings), not shared pretraining; latent search/prompt candidate search is not by itself parameter optimization. Explain multi-stage differences. |
| `evaluates_unseen_users`, `evaluates_new_prompts` | Same four values. `yes` requires checked protocol evidence, and notes must say whether it concerns scoring or generation. A held-out image alone does not certify prompt disjointness. |
| `used_for_generation` | Same four values. `yes` means a demonstrated generation/control use; `no` means a scorer only; `not_applicable` is for standalone data assets. A supporting benchmark paper can be `no` without denying that its evaluated baselines generate images. |
| `base_models` | Verified generative backbones as strings. `null` means not verified; `[]` means no method-specific generative backbone applies (e.g. a standalone scoring tool or benchmark definition). Do not list a synthetic-data generator as the trained personalization backbone. |
| `evidence_note`, `limitations`, `conflicts` | Required evidence and limitation strings; `conflicts` is an array (empty if none recorded). State sources' differing claims without silently reconciling them. |
| `related_ids` | Array of existing IDs; no self-links. Prefer reciprocal parent/asset relationships. |
| `dataset_details` | `null` if not a dataset-focused entry; otherwise object with `name`, `user_identity`, `feedback`, `size_note`, `evaluation_note` and `origin` (same enum as user_data_origin, specific to this dataset rather than the method’s full training/evaluation mix). Explicitly label users, images, ratings, pairs, prompts and testcases; attribute counts to a release/version. |
| `official_code_url`, `project_url`, `data_url`, `model_url` | Optional HTTP(S) links or `null`; null is unverified/unknown unless a companion status says not applicable. Keep a known inaccessible official URL with an explicit status instead of deleting its provenance. |
| `code_status`, `code_note` | Status: `available`, `partial`, `announced`, `inaccessible`, `not_found`, `unverified`, `not_applicable`. Available means code was identified, not executed. Partial must state missing components. Not found is rendered as “Not found as of [date]”. |
| `short_name` | Optional verified acronym/readable label; not another bibliographic title. |
| `reading_order`, `reading_reason` | Optional positive integer and explanation for the generated Start here route; recommendation is a teaching choice, not ranking. |

Paper records additionally carry:

| Fields | Rule |
| --- | --- |
| `authors` | Ordered array of verified names, preferably `Family, Given` for BibTeX. Do not use an invented author list or `et al.`. |
| `first_publication_date` | Earliest verified public version, precision `YYYY`, `YYYY-MM` or `YYYY-MM-DD`; `null` if unverified. Never fill missing day/month. |
| `first_publication_date_note` | Explain the event/version supporting the date and any unresolved earlier-public-version question. An arXiv v1 date and a conference year are different facts. |
| `publication_year`, `venue`, `publication_status` | Year of the verified cited version (or accepted venue year); venue null for unverified formal venue. Status: `preprint`, `submitted`, `accepted`, `published`, `withdrawn`, `unknown`. An OpenReview page or author claim alone is not a verified acceptance. |
| `arxiv_id`, `doi` | ID without URL prefix; DOI bare. `null` means not found/verified. Do not guess DOI or confuse an arXiv DOI with a publisher DOI. |
| `bibtex` | `null` if insufficient verified metadata; else `{key, entry_type, container, pages, source_url}`. Types: `article`, `inproceedings`, `misc`; pages and container may be null. Canonical title/authors/year are reused, not copied into a second schema. |

Prefer official exported BibTeX. Check its title, author order, venue and year against the paper, and preserve only verified fields. `source_url` must appear among checked sources. Minimal entries can be constructed from verified arXiv metadata when no official export is available. An accepted paper without verified proceedings uses a minimal entry with an acceptance note, rather than fabricated volume/pages. Citation keys remain stable when status changes.

### Controlled categories and tags

Categories: `history-conditioned-generation`, `user-conditioned-generation`, `interactive-preference-generation`, `personalized-reward-guided-generation`, `personalized-generation-benchmark`, `personalized-aesthetic-assessment`, `user-level-preference-data`, `personalized-preference-model`, `population-preference-alignment`, `cohort-conditioned-generation`, `style-customization`, `subject-customization`. Cohort-conditioned generation is an adjacent comparison where user groups or item-interest selection steer content without establishing individual visual taste.

Tasks: `generation`, `editing`, `preference_prediction`, `evaluation`.

Signals: `likes`, `likes_dislikes`, `ratings`, `pairwise`, `rankings`, `natural_language`, `implicit_history`, `reference_target`.

Methods: `prompt_rewriting`, `user_representation`, `adapter_fine_tuning`, `reward_guidance`, `retrieval_in_context`, `active_elicitation`. `reward_guidance` includes candidate ranking and preference-aware sampling, not just differentiable reward models. Empty methods means no generation/personalization mechanism applies to the standalone data record.

Evaluation: `target_user_study`, `third_party_human`, `personalized_scorer`, `generic_reward`, `similarity_proxy`, `llm_judge`, `simulation`, `held_out_user_ratings`, `online_engagement`. Held-out ratings are observations, not necessarily users unseen in training; use the separate split field for that distinction. Online engagement means observed behavioral outcomes such as CTR or conversions; it must not be relabeled as a target-user aesthetic preference study.

Source kinds: `paper`, `proceedings`, `conference_decision`, `author_project`, `official_repository`, `dataset_card`, `model_card`, `publisher_metadata`. The last is publisher-deposited bibliographic metadata from a DOI registry, not a third-party paper summary.

### Unknown is not inapplicable

Use `unclear` for unresolved technical yes/no questions and `not_applicable` where the question does not apply. `no` is a checked negative, not “I did not look.” Nullable bibliographic facts mean unverified; fields absent from non-paper records are inapplicable. Empty `conflicts` means no conflict recorded, not proof that none exists. `dataset_details: null` means this record does not carry a dataset description.

## Source and link checks

Offline validation checks JSON types/enums/dates, unique IDs, relations, canonical arXiv IDs and DOI duplicates, exact/similar titles, source provenance, local links and BibTeX keys. Near titles yield warnings. It does **not** prove that a scientific statement is correct, that an external URL works, or that a repository contains a complete reproducible implementation.

When manually probing a link, record the date and observation: 404/410 response, redirect destination, 401 authentication, 403 access restriction, 429 rate limit, timeout, or unverified. A 403 or timeout is not a dead link. A GitHub 404 may also conceal a private resource. Never record all links as passed unless they were actually checked. Keep failed access observations separate from successful metadata evidence and retry only when useful.
