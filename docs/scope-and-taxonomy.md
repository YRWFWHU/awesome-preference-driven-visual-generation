# Scope and taxonomy

This is a working curation policy. It is not presented as a settled terminology standard.

## Decision rule

Identify the user, the observed signal, the current task and the mechanism by which that user's information changes the output. Ask whether the evidence is used to infer/express individual preferences or simply specifies a target subject or style.

| Layer | Admit when | Keep the distinction explicit |
| --- | --- | --- |
| Core methods | Individual signals control actual visual generation/editing, prompt search, adaptation or sampling | A generation experiment is required; prediction accuracy alone is insufficient |
| Core supporting resources | A resource directly supports user-specific visual scoring, data collection or evaluation | A score predictor, dataset and benchmark are not additional generation methods |
| Related but distinct | A representative style/identity, cohort-conditioned or pooled preference baseline clarifies the boundary | Do not count these records as core; do not expand into a generic diffusion bibliography |

Text-to-image generation is the focus. Image editing and narrow interactive attribute control can be admitted with an explicit scope limitation. Ordinary recommendation, language-only personas, generic diffusion, video and 3D are not included by default. Recommender-derived histories are admissible if the work actually uses them for visual generation, as in [PMG](https://arxiv.org/abs/2404.08677).

## Multi-label mechanisms

Mechanism tags describe implementation choices, not exclusive schools. A method can combine prompt rewriting, user representations, parameter adaptation, reward/sampling guidance, retrieval/in-context conditioning and active elicitation. `reward_guidance` includes user-conditioned scoring for candidate selection and sampling guidance; it does not imply a trained reward model or reinforcement learning.

Signals are also multi-label. Natural-language preferences can explain likes/dislikes; ratings can induce comparisons. Conversion between formats must not hide the original collection process. `reference_target` denotes a specified reproduction target rather than automatically treating reference images as revealed preferences.

A user embedding held constant over time may still interact with each new prompt. For example, [Premier](https://arxiv.org/abs/2603.20725) combines user embeddings with prompt tokens. Do not infer prompt independence from the word “embedding.”

## Border cases in this catalog

| Case | Decision and reason |
| --- | --- |
| [PrefGen (relative attributes)](https://arxiv.org/abs/2304.00185) | Core, narrowly: responses identify a session-specific attribute preference. This is not evidence of general T2I preference-history transfer. |
| [StyleDrop](https://arxiv.org/abs/2306.00983) | Adjacent: tuning to a designated style with iterative feedback overlaps preference learning, but broad individual taste inference is not the demonstrated task. |
| [DreamBooth](https://arxiv.org/abs/2208.12242) | Adjacent: the images identify a subject to preserve. A user owning that subject does not make its identity a model of their taste. |
| [Pick-a-Pic / PickScore](https://arxiv.org/abs/2305.01569) | Paper adjacent for pooled scoring; the separately linked dataset is supporting because user IDs allow user-level histories. |
| [LAPIS](https://arxiv.org/abs/2504.07670) | Supporting: individual artwork-score prediction; no generator steering demonstrated in this record. |
| [PAMELA](https://arxiv.org/abs/2604.07427) and [PIGReward](https://arxiv.org/abs/2511.19458) | Core papers because their experiments include personalized generation control; their scoring role alone would place them in supporting. |
| [PerFusion](https://arxiv.org/abs/2503.22182) | Core: individual merchants supply design preferences. Its group-level objective compares a set of candidate images for one person; the downstream shopper is a different actor. |
| [BGGEN](https://arxiv.org/abs/2408.12392) | Core, narrowly: contextual user/item/placement features choose a generation prompt. Shared bandit learning and a small prompt pool limit the claim to contextual background personalization. |
| [CG4CTR](https://arxiv.org/abs/2401.10934) / [KDD banners](https://arxiv.org/abs/2403.05578) | Adjacent cohort-conditioned generation: user-group prompts or affinity-selected products do not establish individual aesthetic conditioning within a fixed task. |
| [CAIG](https://arxiv.org/abs/2502.06823) | Adjacent pooled CTR optimization; Appendix A.5 explicitly distinguishes this from individual personalization. |

These are maintainer classification judgments based on the cited tasks. A paper is counted once even if it spans several roles. A separately registered dataset/tool is linked with `related_ids` and counted as a non-paper resource.

## Evidence is not a single ladder

Use several dimensions rather than one quality rank:

1. History resemblance: output shares features with historical images.
2. Generic quality: output receives better pooled human or model scores.
3. Conditional sensitivity: changing a user condition changes output.
4. Target-user preference: the actual user favors output produced with their own condition, preferably against both a generic and a mismatched-user control.

None logically implies all the others. Negative controls and counterfactual histories can help distinguish content copying from a meaningful user effect. Real-user studies have sampling and protocol limitations; synthetic users offer controlled tests but inherit their construction assumptions. User comments can add reasons for liking, but those reasons also need validation.

Online engagement is another evidence dimension, recorded separately as `online_engagement`. Clicks can respond to product relevance, display placement and marketing context as well as visual taste. A generated-vs-original-image A/B test and a personalized-vs-random-generation A/B test support different claims.

Unclear cases belong in the [backlog](search-backlog.md) until the identity, source or task boundary can be resolved. If a verified record has unknown technical details, use explicit unknown values rather than inventing them.
