# Maintenance notes

This log describes curation decisions. Canonical paper metadata and source-check dates live in [resources.json](../data/resources.json); counts and citations are generated from it.

## 2026-09-17 Asia/Shanghai / 2026-09-16 UTC

Added nine papers after reading original methods and evaluation protocols. This selective update includes papers first posted through September 11, 2026; it is not a completeness claim.

| Group | Additions | Curation decision |
| --- | --- | --- |
| September advertising generation | [AdMan](../README.md#adman), [advertising personalization user study](../README.md#advertising-personalization-user-study) | Related but distinct papers: technical feasibility versus recipients’ responses. Keep separate records and reciprocal links; do not pool their participants as independent samples. |
| Generation and editing | [ZIPP](../README.md#zipp), [DPPMG](../README.md#dppmg), [C-DPO editing](../README.md#collaborative-dpo-editing), [FedPAIE](../README.md#fedpaie) | Distinguish persona inference, history-conditioned synthesis, preference-guided editing and color enhancement. |
| Supporting prediction/data | [PALATE](../README.md#palate), [PRAC](../README.md#prac), [XPASS-Vis](../README.md#xpass-vis) | Candidate ranking or aesthetic prediction does not establish new image generation. |

Verified DPPMG’s SIGIR 2026 metadata through publisher-deposited Crossref data and C-DPO’s NeurIPS 2025 metadata through official proceedings BibTeX. ECCV’s accepted list links ZIPP’s exact author project under a shorter title; acceptance is recorded without inventing proceedings metadata. PRAC’s ACM MM acceptance remains an author claim pending an official decision or proceedings source.

Checked implementation inventories for C-DPO and FedPAIE; both contain code, which was not executed. PRAC currently exposes documentation rather than its promised implementation. Revisited the PrefGen multimodal project (code/model still announced) and PAMELA predictor repository (HTTP 404 again); these checks produced no availability upgrade. Unrelated existing records retain their previous source dates.

REBECA remains in the [backlog](search-backlog.md): publisher metadata for the conference paper names one author, while the expanded arXiv version names four. UnifiedReward-Flex was reviewed as a boundary case: its demonstrated criteria adapt to visual content and prompts, without establishing conditioning on an individual user’s taste.

Validation: rebuild README/BibTeX, run offline schema/link checks, verify generated-file consistency, and run the existing tool tests. These checks cover repository integrity, not scientific reproduction or universal external-link availability.

### IR conference expansion (same check date)

Searched WWW, SIGIR and KDD using conference names, personalized image/content generation, generative outfit recommendation, creative optimization and item-design terminology. The arXiv API helper and primary web sources contributed; no local PDF library was available. Existing PMG and DPPMG were retained without duplicate records.

Added ten papers: Pigeon, DiFashion, FashionDPO, DualFashion, PerFusion, BGGEN and AdBooster as core methods; CG4CTR, CAIG and the KDD e-commerce-banner pipeline as adjacent comparisons. Formal publication metadata was checked against publisher-deposited Crossref records or proceedings. AdBooster is a Fashion x RecSys workshop paper with a 2025 proceedings chapter, not a RecSys 2023 main-track paper.

Added a [Chinese conference reading map](ir-conference-guide.zh-CN.md), the `cohort-conditioned-generation` category and the `online_engagement` evaluation tag. These distinguish group affinity and aggregate CTR from individual aesthetic feedback. Similarity metrics, automatically generated DPO labels and third-party raters remain explicit in the records.

Reviewed TAME as out of scope: its image generator constructs inputs for personalized VQA. PCG, RAGAR, Uni-AdGen and other incomplete checks remain in the backlog. Reading the indexed first page of the RecSys REBECA manuscript clarifies that its single-author version explicitly credits the earlier collaborative paper; full version comparison remains pending after direct institutional PDF retrieval returned 403/429.

Public implementation inventories were checked for Pigeon, DiFashion, FashionDPO, DualFashion, CG4CTR and CAIG. Code was not executed; CG4CTR remains partial. No official implementation was identified for the two KDD generation papers, BGGEN or AdBooster in this pass.
