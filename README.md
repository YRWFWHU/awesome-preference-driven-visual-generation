# Awesome Preference-Driven Visual Generation

A curated collection of research on user-specific preference modeling, personalization, and evaluation for visual generation.

The emphasis is **user-specific preference-driven personalization for text-to-image generation**. This is a selective research map, maintained through evidence-backed contributions. It is not an exhaustive survey or a benchmark leaderboard. Each record carries its own source-check date and limitations. Papers have not been independently reproduced by this repository.

[中文研究指南](docs/research-guide.zh-CN.md) · [WWW / SIGIR / KDD reading map](docs/ir-conference-guide.zh-CN.md) · [Scope and taxonomy](docs/scope-and-taxonomy.md) · [Structured catalog](data/resources.json) · [BibTeX](references.bib) · [Maintenance notes](docs/updates.md) · [Search backlog](docs/search-backlog.md) · [Contribute](CONTRIBUTING.md)

## Contents

- [What counts as preference-driven personalization?](#what-counts-as-preference-driven-personalization)
- [Catalog and counts](#catalog)
- [Start here](#start-here)
- [Core methods](#core-methods)
- [Core supporting resources](#core-supporting-resources)
- [Related but distinct](#related-but-distinct)
- [Datasets and benchmarks](#datasets-and-benchmarks)
- [Evaluation pitfalls](#evaluation-pitfalls)
- [Maintenance and citation](#maintenance-and-citation)

## What counts as preference-driven personalization?

For this collection, **preference-driven personalization** means inferring or using a particular user's preferences from their history, feedback, or descriptions to make generated results better fit that user while satisfying the current task. This is an operational definition for curation, not a claim that the field has adopted one universal definition.

Signals may include liked images, likes/dislikes, ratings, pairwise choices, natural-language preferences, or implicit behavior. Negative feedback, reward models, reinforcement learning and DPO are not prerequisites.

- **Core methods:** actually generate or edit images, adapt a generator, rewrite prompts, or guide sampling using individual preferences. Session-specific elicitation can qualify, but its narrower scope must be stated.
- **Core supporting resources:** personalized preference/aesthetic predictors, user-level datasets and generation evaluation protocols. A predictor alone is not a demonstrated generation method.
- **Related but distinct:** a small set of style/subject customization and population-alignment baselines. They are excluded from core-method counts.

Identity fidelity is not evidence of user-preference alignment. Using a preference loss is not evidence of user conditioning. Style may be part of a preference: a style reference supplied as the target and a historical image used as evidence of taste serve different roles, with some overlap. A fixed user embedding can still interact with the current prompt. Real-user evaluation affects evidence strength, rather than being the only admission criterion. Shared attributes of liked images are not necessarily the reasons for liking them.

<!-- BEGIN GENERATED CATALOG -->

## Catalog

Generated from [data/resources.json](data/resources.json). Dates below are source checks, not a claim of exhaustive coverage.

| Scope | Papers | Other resources |
| --- | ---: | ---: |
| Core methods | 27 | 0 |
| Core supporting resources | 6 | 3 |
| Related but distinct | 7 | 0 |

Per-record verification dates: 2026-09-16, 2026-09-21. Related resource records are not counted as additional papers.

## Start here

One possible route, chosen for contrasting questions rather than priority or rank:

- [Tailored Visions](#tailored-visions): See how implicit generation history becomes prompt rewriting, and why a history is not a dislike label.
- [ViPer](#viper): Inspect natural-language preference elicitation and the own-user versus other-user comparison.
- [PPD](#ppd): Study few-shot conditioning with distinct unseen-user and held-out-caption splits; inspect the model-judge protocol.
- [Premier](#premier): Contrast amortized user conditioning with explicit new-user optimization and prompt-dependent preference modulation.
- [PIPBench](#pipbench): Inspect what a benchmark actually treats as preference ground truth and how simulated profiles differ from people.
- [PAMELA](#pamela): Connect personalized rating prediction to generation steering; separate prediction splits from target-user evaluation.

## Core methods

| Work | Year / status | Signal; mechanism | Official resources | Contribution / boundary |
| --- | --- | --- | --- | --- |
| <a id="advertising-personalization-user-study"></a>[Enabling and Understanding Personalization in AI-Generated Advertising Imagery](https://arxiv.org/abs/2609.12697) | 2026 · arXiv · preprint | natural language; user representation, prompt rewriting | Code: Not found as of 2026-09-16 | Generates advertising images from individual survey profiles and studies how personalization intensity affects the recipients’ responses. |
| <a id="adman"></a>[I Am AdMan: A Pipeline for Automatic Generation of Personalized Advertising Imagery](https://arxiv.org/abs/2609.12694) | 2026 · arXiv · preprint | natural language; user representation, prompt rewriting | Code: Not found as of 2026-09-16 | Turns individual customer profiles into personalized advertising scenes, with product references and an artifact-checking agent. |
| <a id="fedpaie"></a>[Learning Color Grading, No Photo Sharing: Federated Aesthetic Preference Learning for Personalized Image Enhancement](https://arxiv.org/abs/2607.27659) | 2026 · arXiv · preprint | ratings; user representation, reward guidance | [Code](https://github.com/LouckXu/FedPAIE) | Calibrates a federated aesthetic scorer for each user and uses it to adapt a lightweight color-grading enhancer. |
| <a id="papa"></a>[PAPA: Online Personalized Active Preference Alignment](https://arxiv.org/abs/2607.00486) | 2026 · arXiv · preprint | likes dislikes, ratings; active elicitation | [Code](https://github.com/NasikNafi/papa) · (partial) | Online diffusion fine-tuning from simulated session-specific likes and dislikes. |
| <a id="zipp"></a>[ZIPP:Zero-shot Image Personalization from Personas](https://arxiv.org/abs/2606.08841) | 2026 · ECCV 2026 · accepted | natural language, implicit history; user representation, prompt rewriting | [Project](https://behavior-in-the-wild.github.io/zipp.html) · Code: Not found as of 2026-09-16 | Uses natural-language personas to rewrite prompts for frozen image generators, with graph-mined histories or survey-derived profiles. |
| <a id="dualfashion"></a>[Dual-Diffusional Generative Fashion Recommendation](https://arxiv.org/abs/2605.17357) | 2026 · SIGIR 2026 · published | implicit history; user representation | [Code](https://github.com/LinkMingzhe/DualFashion) | Uses a dual image/text diffusion Transformer to generate fashion item images and structured captions, conditioned on attribute-level preferences mined from the user’s item history. |
| <a id="dppmg"></a>[Discrete Preference Learning for Personalized Multimodal Generation](https://arxiv.org/abs/2604.20434) | 2026 · SIGIR 2026 · published | ratings, implicit history; user representation, reward guidance | Code: Not found as of 2026-09-16 | Quantizes graph-based user preferences into modality-specific tokens that condition personalized images and text. |
| <a id="pamela"></a>[Personalizing Text-to-Image Generation to Individual Taste](https://arxiv.org/abs/2604.07427) | 2026 · arXiv · preprint | ratings; user representation, prompt rewriting, reward guidance | [Code](https://github.com/PAMELA-bench/PAMELA_Predictor) · [Project](https://pamela-bench.github.io/) · (inaccessible) | Predicts individual aesthetic ratings and uses the personalized predictor to select iteratively rewritten prompts. |
| <a id="premier"></a>[Premier: Personalized Preference Modulation with Learnable User Embedding in Text-to-Image Generation](https://arxiv.org/abs/2603.20725) | 2026 · CVPR 2026 · published | likes; user representation, adapter fine tuning | [Code](https://github.com/120L020904/Premier) · [Model](https://huggingface.co/pino10010/Premier) | Learns user embeddings and prompt-dependent adapters, then optimizes new users as combinations of learned embeddings. |
| <a id="prefgen-multimodal"></a>[PrefGen: Multimodal Preference Learning for Preference-Conditioned Image Generation](https://arxiv.org/abs/2512.06020) | 2025 · arXiv · preprint | likes dislikes; user representation, adapter fine tuning | [Project](https://prefgen.github.io/) · Code: announced | Extracts liked/disliked visual preferences with an MLLM and conditions diffusion through aligned user representations. |
| <a id="pigreward"></a>[Personalized Reward Modeling for Text-to-Image Generation](https://arxiv.org/abs/2511.19458) | 2026 · ECCV 2026 · accepted | pairwise, rankings; user representation, reward guidance, prompt rewriting, adapter fine tuning | Code: Not found as of 2026-09-16 | Builds user-conditioned judging criteria and uses personalized feedback to optimize generation prompts. |
| <a id="collaborative-dpo-editing"></a>[Personalized Image Editing in Text-to-Image Diffusion Models via Collaborative Direct Preference Optimization](https://arxiv.org/abs/2511.05616) | 2025 · NeurIPS 2025 · published | likes dislikes; user representation, prompt rewriting, adapter fine tuning | [Code](https://github.com/ConnorDunlop/Personalized-Image-Editing) · [Project](https://personalized-editing.github.io/) | Learns graph-based user preferences and a collaborative DPO prompt policy to drive personalized diffusion edits. |
| <a id="icg"></a>[ICG: Improving Cover Image Generation via MLLM-based Prompting and Personalized Preference Alignment](https://aclanthology.org/2025.emnlp-main.617/) | 2025 · EMNLP 2025 · published | implicit history, ratings, pairwise; prompt rewriting, user representation, adapter fine tuning, reward guidance | Code: Not found as of 2026-09-21 | User-profile embeddings condition cover generation through a shared adapter trained with personalized and generic rewards. |
| <a id="drum"></a>[Draw Your Mind: Personalized Generation via Condition-Level Modeling in Text-to-Image Diffusion Models](https://arxiv.org/abs/2508.03481) | 2025 · ICCV 2025 · published | implicit history, natural language; user representation, adapter fine tuning, reward guidance | [Code](https://github.com/Burf/DrUM) · [Model](https://huggingface.co/Burf/DrUM) | Combines user profiling and a reusable condition-space adapter to personalize diffusion generation. |
| <a id="drc"></a>[DRC: Enhancing Personalized Image Generation via Disentangled Representation Composition](https://arxiv.org/abs/2504.17349) | 2025 · ACM MM 2025 · published | implicit history, ratings, reference target; user representation, adapter fine tuning | [Code](https://github.com/ZhengWwwq/DRC) | Separates historical style and reference semantics through reconstruction, then composes them to guide personalized generation. |
| <a id="fashiondpo"></a>[FashionDPO:Fine-tune Fashion Outfit Generation Model using Direct Preference Optimization](https://arxiv.org/abs/2504.12900) | 2025 · SIGIR 2025 · published | implicit history, pairwise; user representation, adapter fine tuning | [Code](https://github.com/LinkMingzhe/FashionDPO) | Fine-tunes the history-conditioned DiFashion generator with DPO pairs derived from automatic quality, outfit-compatibility and personalization feedback. |
| <a id="perfusion"></a>[Sell It Before You Make It: Revolutionizing E-Commerce with Personalized AI-Generated Items](https://arxiv.org/abs/2503.22182) | 2026 · KDD 2026 · published | likes dislikes, rankings; user representation, reward guidance | Code: Not found as of 2026-09-16 | Uses merchant profiles and selections among candidate images to train personalized reward and diffusion models for product design. |
| <a id="ppd"></a>[Personalized Preference Fine-tuning of Diffusion Models](https://arxiv.org/abs/2501.06655) | 2025 · CVPR 2025 · published | pairwise; user representation, adapter fine tuning | [Code](https://github.com/Asap7772/Personalized-Text-To-Image-Diffusion) · (partial) | Conditions diffusion preference tuning on representations inferred from a user’s comparison examples. |
| <a id="pasta"></a>[Preference Adaptive and Sequential Text-to-Image Generation](https://arxiv.org/abs/2412.10419) | 2025 · ICML 2025 · published | rankings, natural language; prompt rewriting, user representation, active elicitation | [Data](https://www.kaggle.com/datasets/googleai/pasta-data) · Code: unverified | Learns a value-based policy to select prompt-expansion slates from sequential user choices. |
| <a id="pigeon"></a>[Personalized Image Generation with Large Multimodal Models](https://arxiv.org/abs/2410.14170) | 2025 · WWW 2025 · published | implicit history, ratings, reference target; user representation, adapter fine tuning | [Code](https://github.com/YiyanXu/Pigeon) | Filters visual tokens in user histories with reference-aware masks, learns personalized image tokens using LaVIT, and decodes them with SDXL; alignment combines history reconstruction and pseudo-preference DPO. |
| <a id="bggen"></a>[Dynamic Product Image Generation and Recommendation at Scale for Personalized E-commerce](https://arxiv.org/abs/2408.12392) | 2024 · RecSys 2024 Industry · published | implicit history; reward guidance | Code: Not found as of 2026-09-16 | Uses a contextual bandit to select background-generation prompts from user, product and placement features. |
| <a id="viper"></a>[ViPer: Visual Personalization of Generative Models via Individual Preference Learning](https://arxiv.org/abs/2407.17365) | 2024 · ECCV 2024 · published | likes dislikes, natural language; user representation, reward guidance | [Code](https://github.com/EPFL-VILAB/ViPer) · [Project](https://viper.epfl.ch/) | Converts free-form comments about liked and disliked images into attributes that guide personalized sampling. |
| <a id="pmg"></a>[PMG : Personalized Multimodal Generation with Large Language Models](https://arxiv.org/abs/2404.08677) | 2024 · The Web Conference 2024 · published | implicit history, natural language; prompt rewriting, user representation, adapter fine tuning | [Code](https://github.com/mindspore-lab/models/tree/master/research/huawei-noah/PMG) · (inaccessible) | Turns individual behavior histories into keywords and soft embeddings for personalized image generation. |
| <a id="difashion"></a>[Diffusion Models for Generative Outfit Recommendation](https://arxiv.org/abs/2402.17279) | 2024 · SIGIR 2024 · published | implicit history; user representation | [Code](https://github.com/YiyanXu/DiFashion) | Generates actual fashion-item images, either completing an outfit or producing an entire outfit, conditioned on a user’s historical fashion interactions. |
| <a id="tailored-visions"></a>[Tailored Visions: Enhancing Text-to-Image Generation with Personalized Prompt Rewriting](https://arxiv.org/abs/2310.08129) | 2024 · CVPR 2024 · published | implicit history; prompt rewriting, retrieval in context | [Code](https://github.com/zzjchen/Tailored-Visions) | Rewrites a prompt using the individual’s earlier prompts and image-generation history. |
| <a id="adbooster"></a>[AdBooster: Personalized Ad Creative Generation Using Stable Diffusion Outpainting](https://arxiv.org/abs/2309.11507) | 2025 · Fashion x RecSys 2023 (2025 proceedings) · published | natural language; user representation, prompt rewriting, reward guidance | Code: Not found as of 2026-09-16 | Outpaints product backgrounds using a user’s shopping query and context, with shared domain tuning. |
| <a id="prefgen-relative-attributes"></a>[PrefGen: Preference Guided Image Generation with Relative Attributes](https://arxiv.org/abs/2304.00185) | 2023 · arXiv · preprint | pairwise; active elicitation, reward guidance | [Code](https://github.com/helblazer811/PrefGen) | Elicits session-specific attribute preferences through comparisons for StyleGAN face editing and generation. |

## Core supporting resources

| Work | Year / status | Signal; mechanism | Official resources | Contribution / boundary |
| --- | --- | --- | --- | --- |
| <a id="palate"></a>[PALATE: Personalized Aesthetic Learning through Adaptive Taste Evolution for Multi-User Portrait Retouching](https://arxiv.org/abs/2608.18622) | 2026 · arXiv · preprint | rankings; user representation, reward guidance | Code: Not found as of 2026-09-16 | Learns shared, cohort and individual rewards to rank existing expert-retouched portrait candidates; no new image synthesis is demonstrated. |
| <a id="prac"></a>[Personalized Image Aesthetic Assessment via Preference-rich Sample Mining and Cohort Merging](https://arxiv.org/abs/2607.15752) | 2026 · arXiv · preprint | ratings; user representation, adapter fine tuning | [Code](https://github.com/yzc-ippl/PRAC) · [Project](https://yzc-ippl.github.io/PRAC/) · Code: announced | Selects informative aesthetic examples and merges models from similar users to predict individual image ratings. |
| <a id="pipbench"></a>[PIPBench: A Profile-Inclusive Framework for Personalized Image Generation Evaluation](https://arxiv.org/abs/2607.06440) | 2026 · ECCV 2026 · accepted | likes; retrieval in context, prompt rewriting | [Code](https://github.com/wuyuhang05/PIPBench) · [Project](https://wuyuhang05.github.io/PIPBench/) · [Data](https://huggingface.co/datasets/AirRain03/PIPBench) | Evaluates generation from preferred-image histories using real-user profiles and synthetic agents. |
| <a id="xpass-vis"></a>[XPASS-Vis: A Dataset for Cross-Domain Personalized Image Aesthetic Assessment](https://arxiv.org/abs/2606.15629) | 2026 · arXiv · preprint | ratings; user representation | Code: announced | Introduces shared-user ratings across artwork, fashion and landscapes to study cross-domain personalized aesthetic prediction. |
| <a id="designpref"></a>[DesignPref: Capturing Personal Preferences in Visual Design Generation](https://arxiv.org/abs/2511.20513) | 2025 · arXiv · preprint | pairwise, natural language; adapter fine tuning, retrieval in context | Code: unverified | Studies designer-specific visual judgments using UI comparisons, personalized UIClip tuning and retrieval-conditioned judges. |
| <a id="lapis"></a>[LAPIS: A novel dataset for personalized image aesthetic assessment](https://arxiv.org/abs/2504.07670) | 2025 · CVPR Workshops 2025 (CVEU) · published | ratings; user representation | [Project](https://github.com/Anne-SofieMaerten/LAPIS) | Provides artwork ratings and rater attributes for studying individual aesthetic-score prediction. |
| <a id="viper-proxy"></a>[ViPer personalized proxy metric](https://github.com/EPFL-VILAB/ViPer) | tool | likes dislikes; retrieval in context | [Code](https://github.com/EPFL-VILAB/ViPer) | Scores a query image conditioned on liked and disliked context images. |
| <a id="pick-a-pic-dataset"></a>[Pick-a-Pic user-linked comparisons](https://github.com/yuvalkirstain/PickScore) | dataset | pairwise | [Data](https://huggingface.co/datasets/yuvalkirstain/pickapic_v2) | Collects real-user image choices with user identifiers that can be grouped into histories. |
| <a id="pamela-dataset"></a>[PAMELA dataset](https://huggingface.co/datasets/bethgelab/PAMELA) | dataset | ratings | [Data](https://huggingface.co/datasets/bethgelab/PAMELA) | Publishes generated images with participant-linked ratings and separate seen/unseen-user splits. |

## Related but distinct

| Work | Year / status | Signal; mechanism | Official resources | Contribution / boundary |
| --- | --- | --- | --- | --- |
| <a id="caig"></a>[CTR-Driven Advertising Image Generation with Multimodal Large Language Models](https://arxiv.org/abs/2502.06823) | 2025 · WWW 2025 · published | implicit history; prompt rewriting, reward guidance, adapter fine tuning | [Code](https://github.com/JD-GenX/CAIG) | Optimizes advertising backgrounds with aggregate CTR rewards and product-centric prompt preference optimization. |
| <a id="ecommerce-banners"></a>[Chaining Text-to-Image and Large Language Model: A Novel Approach for Generating Personalized e-commerce Banners](https://arxiv.org/abs/2403.05578) | 2024 · KDD 2024 · published | implicit history; prompt rewriting | Code: Not found as of 2026-09-16 | Selects a product through user/cohort affinity, then converts product attributes into a banner-generation prompt. |
| <a id="cg4ctr"></a>[A New Creative Generation Pipeline for Click-Through Rate with Stable Diffusion Model](https://arxiv.org/abs/2401.10934) | 2024 · WWW 2024 Companion · published | implicit history; prompt rewriting, reward guidance, adapter fine tuning | [Code](https://github.com/HaoYang0123/Creative_Generation_Pipeline) · (partial) | Generates product backgrounds using cohort-conditioned prompts and CTR-guided training. |
| <a id="diffusion-dpo"></a>[Diffusion Model Alignment Using Direct Preference Optimization](https://arxiv.org/abs/2311.12908) | 2024 · CVPR 2024 · published | pairwise; adapter fine tuning | [Code](https://github.com/SalesforceAIResearch/DiffusionDPO) | Optimizes diffusion likelihood differences from pooled human image comparisons. |
| <a id="styledrop"></a>[StyleDrop: Text-to-Image Generation in Any Style](https://arxiv.org/abs/2306.00983) | 2023 · NeurIPS 2023 · published | reference target, pairwise; adapter fine tuning | [Project](https://styledrop.github.io/) · Code: Not found as of 2026-09-16 | Adapts a text-to-image model to a supplied style example, with optional iterative feedback. |
| <a id="pick-a-pic"></a>[Pick-a-Pic: An Open Dataset of User Preferences for Text-to-Image Generation](https://arxiv.org/abs/2305.01569) | 2023 · NeurIPS 2023 · published | pairwise; reward guidance | [Code](https://github.com/yuvalkirstain/PickScore) | Introduces crowdsourced image comparisons and PickScore, a general preference scorer used for ranking. |
| <a id="dreambooth"></a>[DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation](https://arxiv.org/abs/2208.12242) | 2023 · CVPR 2023 · published | reference target; adapter fine tuning | [Project](https://dreambooth.github.io/) · [Data](https://github.com/google/dreambooth) · Code: Not found as of 2026-09-16 | Fine-tunes a generator to reproduce a specific subject in new text-described contexts. |

## Datasets and benchmarks

These descriptions summarize the verified releases or paper protocols; a real-user history does not by itself imply a target-user generation study. Access and licenses belong to the providers.

| Resource / parent paper | User IDs and feedback | Origin | Reported size (units explicit) | Evaluation / access caveat |
| --- | --- | --- | --- | --- |
| [PIP (Tailored Visions)](#tailored-visions) | User identifiers in histories; Historical prompts and saved generations, not explicit dislike labels | real | 3,115 users; 300,237 text-to-image history records (Section 3) | Offline proxy evaluation plus an online target-user study; PIP and PIPBench are different datasets. |
| [PIGBench](#pigreward) | Per-user preference records; Ranking image groups for common prompts | real | 75 user records (paper Section 4) | Real-user judgments; Section 5.6 reuses annotators for generation evaluation. Dataset release not verified in this pass. |
| [PIPBench](#pipbench) | Profile-linked user/agent records; Preferred images; real choices versus simulated ranking | mixed | 76 real users + 175 agents; 1,369 testcases; 1,876 images (project page) | 650 real-user and 719 synthetic-agent testcases. Human calibration and judge agreement are distinct from target-user output preference. |
| [LAPIS](#lapis) | Annotator-linked ratings and personal attributes; Individual aesthetic ratings of artworks | real | 11,723 artwork images (paper abstract) | Prediction benchmark, not a generation user study. Access by request through author repository. |
| [PAMELA released dataset](#pamela-dataset) | participant_id; 199 participants in release card; Individual ratings plus image/user metadata | real | 69,904 ratings; 5,077 images; 199 participants (release card) | Seen/unseen user splits are rating-prediction protocols; generation study belongs to the paper. |
| [Pick-a-Pic](#pick-a-pic-dataset) | User identifiers; verify retained columns for chosen version; Real-user pairwise preferences (ties may be present) | real | Version-specific; no unified count across v1/v2 or filtered histories | Collection records real choices; does not itself evaluate new personalized outputs. v2 access could not be verified (HTTP 401). |
| [PALATE portrait-ranking protocol](#palate) | 25 volunteers with persistent user identities; Rankings of three expert retouches per source portrait | real | Paper: 1,000 PPR10K source portraits, 25,000 rankings and 75,000 derived pairwise comparisons | Joint held-out-user/image evaluation; no standalone public ranking release verified. |
| [XPASS-Vis](#xpass-vis) | Same 129 annotators across three visual domains; Overall aesthetic and nine emotion ratings | real | Paper: 6,526 stimuli; 87,836 user–stimulus interactions | User-level cross-validation plus per-target calibration; data/code announced, not verified released. |
| [ZIPBench](#zipp) | Matched Reddit/Civitai accounts with inferred personas; Behavioral histories and generated images, not a released table of explicit aesthetic choices | real | Paper: 1.5K users and 40K Civitai generations | Persona inference and account matching need scrutiny; no public dataset release verified. |
| [C-DPO editing preference protocol](#collaborative-dpo-editing) | Synthetic profiles; separate real-user survey; Liked/disliked editing attributes | synthetic | Paper: 3,000 synthetic users and 144K preference samples; approximately 2,900/100 train/test users | Repository provides a download script; asset contents and counts were not independently downloaded. |
| [iFashion and Polyvore-U](#difashion) | Dataset user identifiers link outfit/product interactions.; Implicit product/outfit clicks or interactions. | real | Active users have at least five interacted outfits; four-item outfits used after filtering. | 8:1:1 split of interacted outfits; not an explicit held-out-user split. |
| [SER30K-derived histories and MovieLens-Latest-small posters](#pigeon) | Synthetic theme-level sticker users; real MovieLens identifiers.; Same-theme sticker sequences and movie ratings &gt;=4; pseudo-labeled preference pairs for DPO. | mixed | Six interactions per sliding-window sample (five context, one target). | 8:1:1 sample split; sticker reference from another theme, movie reference equals target; no explicit user-disjoint evaluation. |
| [iFashion and Polyvore-U](#fashiondpo) | Real user IDs from historical item/outfit interactions.; Real implicit interaction histories; generated pairwise preferences from automated experts. | mixed | Each epoch samples 1,000 training outfits; seven generated candidates per outfit; five fine-tuning epochs. | Training/test outfit split; five designers score 30 result sets, without a target-user satisfaction test. |
| [iFashion and Polyvore-U with structured captions](#dualfashion) | Real user-history IDs inherited from fashion datasets.; Implicit historical interactions converted into sampled attribute-level preference text. | real | 344,186 iFashion item captions extracted; Polyvore-U categories predicted using an iFashion-trained classifier. | PFITB and GOR automatic metrics; full paper does not specify a disjoint-user split. |
| [PerFusion Pick-a-Pic and industrial protocols](#perfusion) | Pick-a-Pic IDs and merchant profiles; Selections/rejections within one candidate image set | real | Table 1: industrial 54,995 users, 60,616 prompts, 607,328 samples; candidate group size 5 | Private industrial data; record-level split and own-reward evaluation, not an unseen-user study. |

Metadata, source-level dates, split evidence, verified base models, limitations and conflicts are preserved in [the JSON catalog](data/resources.json). No cross-protocol leaderboard is maintained.

<!-- END GENERATED CATALOG -->

## Evaluation pitfalls

The following are different observations: **similarity to history**, **higher overall quality**, **outputs changing with user conditioning**, and **the target user preferring their own personalized outputs**. Report which observation an experiment supports.

- **Content leakage:** similar subjects, repeated artworks, near-duplicate images, or prompts reconstructed from the desired target may reward copying instead of preference transfer. Keep content fidelity and preference fit separate.
- **User and prompt leakage:** hold out users separately from prompts and deduplicate images across history, optimization, validation and evaluation. A held-out image is not automatically a new prompt or an unseen concept. State whether “unseen user” concerns score prediction or generation.
- **Similarity is a proxy:** CLIP/DINO similarity and LPIPS can track repeated content or style. They do not directly measure why a person likes an image.
- **Generic rewards are not personalized rewards:** pooled preference scores may improve all users' average quality while missing individual differences. Include a strong non-personalized baseline and a mismatched-user condition where appropriate.
- **People, proxies and agents:** distinguish the history owner from third-party annotators, model judges and synthetic users. Report who supplied history, who judged outputs and whether a judge saw the full profile. Demographics are not ground-truth preferences.
- **Optimization and evaluation dependence:** evaluating with the same scorer used for optimization can measure reward exploitation. Report held-out judging and prompt adherence, not just the optimized score.
- **Protocol comparability:** do not pool results across datasets, splits, histories, backbones, sampling budgets or raters. Report participant-level uncertainty and missing/tied judgments when available.

These are maintainer synthesis and recommended checks, not assertions that every listed paper has each failure mode. Individual evidence notes point to the checked sources.

## Maintenance and citation

The sole structured catalog is [data/resources.json](data/resources.json). Edit it and regenerate the marked catalog and bibliography; prose outside the markers stays manual. Python 3.10 or later, standard library only:

```bash
python scripts/build.py
python scripts/build.py --check
python scripts/validate.py
python -m unittest discover -s tests
```

Use `python3` if your system does not provide `python`. `--check` never writes files. CI performs offline validation and generation-consistency checks on pushes and pull requests; it does not probe external links. Source access errors and incomplete release/status checks are documented in the [backlog](docs/search-backlog.md). No “all external links passed” claim is made.

To add a paper, follow [CONTRIBUTING.md](CONTRIBUTING.md) or open an issue using the resource template. Verify the paper and its status, explain the individual-user signal, update one JSON record and run the commands above. Preprint and proceedings versions belong to the same record.

For research claims, cite the original papers using [references.bib](references.bib). To acknowledge this collection, use its title, the actual published repository URL, the commit hash and your access date. No invented DOI or unpublished repository URL is supplied.

Original curation, documentation and scripts are dedicated under [CC0-1.0](LICENSE). This dedication does **not** cover linked papers, code, models, datasets, project pages or their assets; those remain subject to their respective licenses. Inclusion is not endorsement or a verification of downstream licensing suitability.
