# WWW、SIGIR、KDD 中的用户偏好驱动视觉生成

检索核验：2026-09-17（北京时间；UTC 2026-09-16）。本轮按会议检索原论文、作者资源和出版信息，结合已有条目去重。下面是选择性阅读地图，不是各届会议的完整目录。结构化元数据仍以 [resources.json](../data/resources.json) 为准。

## 与个人偏好生成直接相关的主线

| 工作 | 正式发表 | 用户信号与生成方式 | 阅读时要检查的证据边界 |
| --- | --- | --- | --- |
| [PMG](https://arxiv.org/abs/2404.08677) | WWW 2024；原已收录 | 从用户交互历史提取偏好，控制多模态内容生成 | 商品/电影兴趣与视觉审美不完全相同 |
| [Pigeon](https://arxiv.org/abs/2410.14170) | WWW 2025；本轮新增 | 从历史图像筛选视觉 token，用 LaVIT 与 SDXL 生成贴纸或海报 | 贴纸用户按主题合成；电影评分是真实的，但喜欢电影不等于喜欢海报画风；MTurk 是第三方推断 |
| [DiFashion](https://arxiv.org/abs/2402.17279) | SIGIR 2024；本轮新增 | 用户服饰历史条件化扩散，同时生成搭配中的多个服装图像 | 生成了真实图像，非商品 ID；按 outfit 切分不等于未见用户；人工评审不是历史拥有者 |
| [FashionDPO](https://arxiv.org/abs/2504.12900) | SIGIR 2025；本轮新增 | 在 DiFashion 上，用画质、搭配和历史相似度的自动反馈做 DPO | 偏好对来自模型，不是用户亲自投票；设计师评价也不等于个人满意度 |
| [DualFashion](https://arxiv.org/abs/2605.17357) | SIGIR 2026；本轮新增 | 从个人历史抽取服饰属性，用双扩散模型联合生成图像和说明文本 | 个性化主要以历史相似度评估；Gemini 评价文本兼容性，未建立目标用户满意度证据 |
| [DPPMG](https://arxiv.org/abs/2604.20434) | SIGIR 2026；原已收录 | 图交互偏好量化成离散 token，驱动图文生成 | 按时间划分交互记录；不能称为用户互斥测试 |
| [PerFusion / AIGI](https://arxiv.org/abs/2503.22182) | KDD 2026；本轮新增 | 商家画像及一组候选图中的选择/拒绝，训练个性化奖励和生成器 | 用户是商家；group-level 指一个人判断多张候选图，不是人口群体；自身奖励分数和下游消费者 CTR 要分开 |

这条文献线索常用 **personalized content generation、generative outfit recommendation、creative optimization、AI-generated items** 等名称，而不总是使用 personalized diffusion。沿这些任务词和交互历史、商家反馈、广告背景等信号检索，可以补充仅从计算机视觉论文出发容易遗漏的工作。

## 相关，但不能混入个人审美方法的论文

| 工作 | 正式发表 | 为什么单独列为 adjacent |
| --- | --- | --- |
| [CG4CTR](https://arxiv.org/abs/2401.10934) | WWW 2024 **Companion** | §4.2.2 为 user group 枚举提示词和广告，再按群体展示；没有建立同一群体内的个人视觉偏好建模 |
| [CAIG](https://arxiv.org/abs/2502.06823) | WWW 2025 | 附录 A.5 明确指出使用全体用户聚合 CTR、缺少个性化；其 preference optimization 不能直接解释成 individual preference |
| [个性化电商 banner](https://arxiv.org/abs/2403.05578) | KDD 2024 | 根据用户/cohort affinity 选商品，再生成商品相关背景；实验评价商品相关性，未证明同一商品下按个人审美生成 |

CTR 是行为结果，有实际部署价值，但它同时受商品相关性、曝光、位置、价格等影响。需要区分“生成图提高 CTR”“个性化比非个性化提高 CTR”和“用户本人更喜欢生成图”三种结论。仓库新增 `online_engagement` 标签，避免把线上点击测试误标成目标用户审美实验。

## RecSys 邻域补充

[BGGEN](https://arxiv.org/abs/2408.12392)（RecSys 2024 Industry）用用户、商品和展示位置特征指导 LinUCB 选择生成背景的提示词。它的第三阶段线上实验专门比较个性化选择与随机选择；这是有界提示池内的上下文个性化，不是学习任意个人审美。

[AdBooster](https://arxiv.org/abs/2309.11507) 根据购物查询与场景 outpaint 商品背景。正式出处是 **Fashion x RecSys 2023 workshop，2025 年出版论文集**，不能写成 RecSys 2023 主会。它用 30 个合成用户画像和 CLIP 分数评估，未测真实购买或目标用户喜好。

REBECA 的单作者 RecSys 2025 论文明确注明它源自多作者早期工作；不是简单的数据库作者漏项。当前四作者 arXiv 版本与该会议文稿应按版本区分，详见 [待核清单](search-backlog.md)，不能把四作者列表直接配给单作者 DOI。

## 建议的阅读顺序与后续核验

先读 **PMG → Pigeon → DPPMG**，比较文本偏好、视觉 token 与离散交互 token。再读 **DiFashion → FashionDPO → DualFashion**，看领域约束、自动偏好反馈和图文联合生成如何衔接。最后对照 **PerFusion 与 BGGEN**，分别理解商家设计反馈和消费者点击上下文。

这是按问题组织的阅读顺序，不是性能排名。尤其要核对：训练与测试是否共享用户、滑窗历史是否重叠、选择反馈是否为真人、新用户是否要优化参数，以及评价者到底是谁。

[TAME](https://arxiv.org/abs/2512.21616) 虽为 KDD 2026 个性化多模态论文，实际评测是记忆与视觉问答；图片生成器用于构造输入数据，因此不收入核心生成方法。PCG、RAGAR、Uni-AdGen 及其他后续线索已进入 [backlog](search-backlog.md)，未完成原文协议或版本核验的不计入正式条目。
