# Search backlog and verification limits

Initial discovery and source checks: **2026-09-16 (UTC)**. This is a selective pass up to that date, not a comprehensive census. Catalog dates record actual reading in this pass; rebuilding does not refresh them. Names below are leads, not accepted metadata, unless explicitly described as follow-up checks on a formal record. They do not enter counts or BibTeX.

Latest incremental pass: **2026-09-17 Asia/Shanghai (2026-09-16 UTC)**; see [maintenance notes](updates.md). Searches extended into July–September, including personalized image generation, aesthetic assessment, editing and advertising. Nine candidates passed full-paper checks, including two September 11 preprints. No claim is made that all papers through the search date were discovered.

A subsequent venue-focused pass on the same date added ten papers from the WWW/SIGIR/KDD/RecSys literature. See the [conference reading map](ir-conference-guide.zh-CN.md); the nine-paper update above describes the earlier pass, not this repository's current total.

## Discovery trail

Queries combined personalized text-to-image generation, individual/user-specific preferences, personalized diffusion, visual preference learning, personalized reward models, aesthetic assessment and user preference benchmarks. The pass searched named leads, then read related-work/reference sections in PPD, ViPer, DrUM, PrefGen, PIPBench and PAMELA. PMG, ViPer, LAPIS and PIGReward were added beyond the initial name list. Forward discovery searched exact titles with later paper/benchmark terms; search hits were only leads, and formal records were checked against primary texts.

The seven initial names were resolved: Tailored Visions, PPD, Premier, PAMELA, PIPBench and DrUM map to the corresponding catalog records; PrefGen maps to **two different papers**. DRUM LiDAR work and the StreamPref dataset generator named PrefGen are unrelated and excluded. Publication/release follow-ups below do not negate verified paper identities.

## Candidates needing fuller checks

| Lead | Discovery source | Missing work before admission |
| --- | --- | --- |
| PARA / Personalized Image Aesthetics Assessment With Rich Attributes | [CVPR paper](https://openaccess.thecvf.com/content/CVPR2022/papers/Yang_Personalized_Image_Aesthetics_Assessment_With_Rich_Attributes_CVPR_2022_paper.pdf) | Found through LAPIS references; complete original metadata, official dataset link and user-split audit before adding a separate record. |
| Personalized Image Generation for Recommendations Beyond Catalogs / REBECA | [arXiv v3](https://arxiv.org/abs/2502.18477), [publisher-deposited metadata](https://api.crossref.org/works/10.1145/3705328.3748757), [institutional conference manuscript](https://deepblue.lib.umich.edu/bitstream/handle/2027.42/199680/3705328.3748757.pdf?sequence=1) | Full arXiv text checked: user/rating-conditioned SD1.5/IP-Adapter synthesis and verifier-proxy evaluation. The indexed conference first page explicitly credits the prior collaborative work; its single author is not merely a metadata omission. Full institutional PDF retrieval returned 403/429. Compare versions before choosing the canonical record; do not pair four arXiv authors with the single-author RecSys DOI. |
| PreferThinker | [arXiv lead](https://arxiv.org/abs/2511.00609) | Read personalized image-assessment protocol, user split and code release before adding a supporting entry. |
| PCG / Personalized Visual Content Generation in Conversational Systems | [NeurIPS 2025 proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/314116cd378bab6283ae19c07a4ea367-Abstract-Conference.html) | Official identity and author code link located; complete conversation-preference, generator and evaluation-protocol reading. Not a WWW/SIGIR paper merely because it is cited there. |
| RAGAR | [AAAI 2026 proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/38553), [arXiv](https://arxiv.org/abs/2505.01657) | Formal 13-author record differs from the current 15-author arXiv list; old search metadata has six. Select a citation version, read full method/splits and inspect official code before admission. Actual venue is AAAI, not SIGIR. |
| Uni-AdGen / Design Your Ad | [CVPR 2026 paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Xu_Design_Your_Ad_Personalized_Advertising_Image_and_Text_Generation_with_CVPR_2026_paper.pdf) | Abstract/intro indicates individual click histories, unlike pooled CTR. Complete methods, evaluation identity, official-code and dataset checks. |
| Generate, Not Recommend: Personalized Multimodal Content Generation | [arXiv lead](https://arxiv.org/abs/2506.01704) | Discovery only; verify formal venue, ordered authors, actual visual-generation protocol and relation to existing PMG/Pigeon/DPPMG records. |
| NaviGen / Navigating User Behavior toward Personalized Multimodal Generation | [arXiv lead](https://arxiv.org/abs/2606.24196) | Primary abstract inspected; full method, evaluation and formal status not yet checked. |
| ADaFuSE | [SIGIR 2026 DOI](https://doi.org/10.1145/3805712.3809836) | Diffusion-generated imagery assists interactive retrieval; individual visual preference learning is not established from the publisher abstract. Read full scope before adding. |
| Earlier Oracle Guided Image Synthesis with Relative Queries | [Alec Helbling CV](https://alechelbling.com/cv.html) | Possible earlier related version of PrefGen (relative attributes). Check the 2022 workshop paper and relationship before changing the canonical earliest-public date or adding another work. |

## Follow-ups on admitted records

| Record / resource | Observation on the check date | Next action |
| --- | --- | --- |
| PrefGen (multimodal) | ArXiv and author project verified; project says code/model coming soon. An [OpenReview forum](https://openreview.net/forum?id=8iGclsodrJ) was located, but browser retrieval returned a verification page. | Verify public decision and earliest public forum date; do not infer ICLR acceptance from a submission PDF. |
| PPD | Author repository releases only the VLM component, not diffusion tuning. Main-text/appendix judge naming and aggregate win-rate descriptions differ in the checked arXiv text. | Keep component-level code status; inspect exact paper version/protocol before quoting a win rate. |
| PAMELA | Paper-linked [predictor repository](https://github.com/PAMELA-bench/PAMELA_Predictor) returned HTTP 404. Release data card was readable. | Recheck code release; retain paper/release-card count discrepancies. No full dataset download/count recomputation performed. |
| PMG | Paper-linked MindSpore repository URL returned HTTP 404. A [candidate author implementation](https://github.com/Suikasxt/PMG) was discovered, but the direct author/publication linkage and implementation/backbone correspondence need further checking. | Do not silently replace the canonical code URL. Author implementation text mentions SD v2.1 while the paper specifies SD v1.5. |
| Pick-a-Pic v2 | Paper and official PickScore repository verified. Direct Hugging Face v2 data-card request returned HTTP 401. | Verify access conditions and retained user-ID schema in the chosen release before planning data use. |
| PIGReward / PIGBench | Paper and ECCV acceptance list verified; [a reward-model card](https://huggingface.co/jeongeunnn/pigreward) was found. Full code/data release and linkage from an author/paper entry point not completed. | Verify official release chain and code/data completeness; do not equate a model card with a full implementation. |
| PIPBench and PIGReward publication | Exact titles found in the official ECCV 2026 accepted-paper list. | Add proceedings metadata only when verified; accepted is not the same as published. |
| StyleDrop | NeurIPS landing-page title differs from its linked PDF title; both point to the same work. Official project supplies style assets; training implementation not found. | Preserve one paper and the title note. Do not label an explicitly unofficial PyTorch implementation as official. |
| PRAC | Paper and author project claim ACM MM 2026 acceptance; repository has README, figure and website docs. | Verify official decision/proceedings and actual implementation/model release; retain announced code status. |
| XPASS-Vis / PALATE | Full user-split and scoring protocols checked. XPASS-Vis promises data/code upon acceptance; no public PALATE ranking release verified. | Verify release links and licenses before listing standalone assets. |
| ZIPP | ECCV accepted list uses a shorter title but links the same project. Appendix G comparison-condition prose differs from Table 15 allocation. | Verify proceedings and any corrected protocol; do not infer own-versus-other persona results from an unmatched table row. |
| AdMan and advertising user study | Both September 11 preprints have actual image-generation pipelines; evaluation goals and author lists differ. No official code release identified. | Track publication/code and the relationship between samples; do not treat technical artifact rates as recipient preference votes. |

## Deliberately limited adjacent coverage

[UnifiedReward-Flex](https://arxiv.org/abs/2602.02380) was checked in full (Sections 3–4): evaluation criteria adapt to the prompt and visual content, and the reward guides image/video generation. The checked experiments do not establish individual-user preference conditioning. Despite “Personalized” in the title, it is not admitted as a core method; the existing population-alignment examples keep adjacent coverage compact.

[TAME](https://arxiv.org/html/2512.21616) ([KDD 2026 publisher metadata](https://api.crossref.org/works/10.1145/3770854.3780214)) studies evolving personal-concept memory and VQA. GPT-Image-1 creates benchmark input images; evaluated outputs are answers. This is not a demonstrated user-preference visual-generation controller, so it is excluded from the catalog.

InstantStyle, StyleAligned, Textual Inversion, ImageReward and AlignProp remain outside this first curated selection. They are not declared nonexistent or irrelevant; the adjacent examples already cover style, subject and pooled preference baselines. If adding one later, complete its metadata/status/official-resource verification first and justify why it adds a distinct boundary or baseline.

## Access limitations

Some CVF pages returned 403 through the browsing tool; direct read-only HTTP retrieval succeeded and exposed their official BibTeX. The large ECCV accepted-paper page exceeded the browser tool's content limit; direct retrieval allowed exact-title checks. Crossref publisher-deposited metadata corroborated PMG's DOI and proceedings after ACM itself returned 403. These successful alternate reads are distinct from inaccessible resources.

No exhaustive external link sweep, dataset download, code execution, model training or experimental replication was performed. A successful page read establishes accessible source content at check time, not reproducibility or ongoing availability. All CI checks are offline.

## 2026-09-21 literature-return pass

DRC, PASTA and DesignPref now have verified catalog records. DesignPref is supporting assessment work; its author-CV workshop listing still needs proceedings verification. PASTA’s paper-linked Kaggle release and full agent implementation remain unaudited.

Additional unresolved discovery: [Personalized Preference Optimization for Text-to-Image Generation using Large Language Models](https://openreview.net/pdf?id=4VzHv5s0Hp) is an anonymous submission; check authorship and possible overlap with admitted prompt-optimization work before adding. [Design LoRA](https://www.sciencedirect.com/science/article/pii/S1474034626007457) appeared in search with a November 2026 issue date: publication availability, methods and scope were not verified. No future-dated publication claim is made here.

- [I-AM-G: Interest Augmented Multimodal Generator for Item Personalization](https://aclanthology.org/2024.emnlp-main.1187.pdf): discovered in the 2026-09-21 topic search; verify complete method, individual-user evaluation, author metadata and code before admission.
