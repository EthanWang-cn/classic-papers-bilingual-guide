# Classic Papers, Bilingual Guides

<div align="center">

**用中英对照的方式，读透 AI 领域最值得读的 100 篇论文。**

[![Papers](https://img.shields.io/badge/papers-5%2F100-blue?style=flat-square)](README.md)
[![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/EthanWang-cn/classic-papers-bilingual-guide?style=social)](https://github.com/EthanWang-cn/classic-papers-bilingual-guide/stargazers)

</div>

---

## 为什么要有这个仓库

读原论文是理解一个领域最快的方式，但大多数经典论文对中文读者有三道坎：

1. **语言关**——专业英文 + 隐含的领域语境，逐句啃非常慢；
2. **上下文关**——论文写作时默认你知道它在回应什么问题（比如 Transformer 默认你熟悉 RNN 的序列依赖），缺了这层背景就读成了"零件说明书"；
3. **取舍关**——论文里哪些是真正的关键创新、哪些是当时的工程补丁、哪些结论今天已经过时，没人告诉你。

这个仓库把每一篇做成一份**可以直接读、读完就能聊**的双语导读 PDF。不是机翻，不是摘要，而是带着判断的精读。

## 每篇的固定结构

> 文件名即论文名，每篇一个 PDF，顺序固定：

| 部分 | 内容 |
|---|---|
| **1. 原文链接** | arXiv / 官方发表地址，以及作者、年份、发表会议等元信息 |
| **2. 逐段翻译** | 英文原文与中文译文逐段对照（EN 灰底 / 译文跟在后面），公式、表格、超参数、引用编号全部保留 |
| **3. 总结对照导读 + 我的理解** | 这篇论文在解决什么问题、它之前的世界是什么样的、核心创新到底"新"在哪、哪些是今天仍在用的东西、哪些已经过时、常见误解、以及**它和后来的模型有什么因果关系**（例如：Transformer 本质上是把 RNN 的时间步递推换成了"所有位置一次性互看"的注意力矩阵运算——为什么这样能并行、为什么又埋下了 O(n²) 的长上下文隐患） |

导读部分不是复述摘要，而是写**真正有用的干货**：读完你应该能回答"这篇论文为什么值得读""它改变了什么""它还留下了什么问题"。

## 选文标准

我们不按引用量堆砌，而是按 **「里程碑意义 × 必读程度 × 思想含量」** 选：

- **改变了技术路线**：发布了之后，后来的工作明显分成"之前"和"之后"（AlexNet、Transformer、BERT）；
- **提出了一个被反复复用的机制**：注意力、残差、GAN 对抗训练、扩散过程等；
- **思想足够干净**：能在十几页里把一个核心想法讲透，值得逐段精读；
- **今天仍在被引用和讨论**：不是考古，是理解当下系统的必要背景。

计划 **100 篇**，按"深度学习革命 → 视觉 → 序列与注意力 → 生成模型 → 自监督与大模型 → 强化学习与多模态"的脉络编排，分批推送。

## 论文清单

状态：✅ 已推送 ｜ 🚧 撰写中 ｜ ⏳ 计划中

| # | 论文 | 年份 | 领域 | 为什么必读 | 状态 |
|---:|---|---:|---|---|---|
| 001 | [Attention Is All You Need](Attention%20Is%20All%20You%20Need.pdf) | 2017 | NLP / 架构 | 去掉循环与卷积，只用注意力建模序列；今天所有大模型的骨架 | ✅ |
| 002 | [ImageNet Classification with Deep Convolutional Neural Networks](ImageNet%20Classification%20with%20Deep%20Convolutional%20Neural%20Networks.pdf) | 2012 | 视觉 | 深度学习复兴的起点：GPU + ReLU + Dropout + 数据增强，ImageNet 错误率骤降 | ✅ |
| 003 | [Generative Adversarial Nets](Generative%20Adversarial%20Nets.pdf) | 2014 | 生成模型 | 用"生成器和判别器互相博弈"绕开显式概率建模，开创对抗生成 | ✅ |
| 004 | [Deep Residual Learning for Image Recognition](Deep%20Residual%20Learning%20for%20Image%20Recognition.pdf) | 2015 | 视觉 / 架构 | 残差连接让上百层网络可训练，几乎是所有现代深层网络的标准件 | ✅ |
| 005 | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](BERT%EF%BC%9APre-training%20of%20Deep%20Bidirectional%20Transformers%20for%20Language%20Understanding.pdf) | 2018 | NLP | 把 Transformer 编码器用于双向预训练，"预训练 + 微调"范式的代表 | ✅ |

<details>
<summary>点击展开后续规划论文（前 30 篇）</summary>

| # | 论文 | 年份 | 方向 |
|---:|---|---:|---|
| 006 | Long Short-Term Memory | 1997 | 序列建模 |
| 007 | Sequence to Sequence Learning with Neural Networks | 2014 | 序列转换 |
| 008 | Neural Machine Translation by Jointly Learning to Align and Translate | 2014 | 注意力 |
| 009 | Very Deep Convolutional Networks for Large-Scale Image Recognition (VGG) | 2014 | 视觉 |
| 010 | Going Deeper with Convolutions (GoogLeNet / Inception) | 2014 | 视觉 |
| 011 | Batch Normalization: Accelerating Deep Network Training | 2015 | 训练技巧 |
| 012 | Faster R-CNN | 2015 | 检测 |
| 013 | You Only Look Once (YOLO) | 2015 | 检测 |
| 014 | Neural Style Transfer / Perceptual Losses | 2015 | 生成 |
| 015 | Auto-Encoding Variational Bayes (VAE) | 2013 | 生成模型 |
| 016 | Playing Atari with Deep Reinforcement Learning (DQN) | 2013 | 强化学习 |
| 017 | Human-level control through deep reinforcement learning | 2015 | 强化学习 |
| 018 | Mastering the game of Go with deep neural networks and tree search | 2016 | 强化学习 |
| 019 | Dropout: A Simple Way to Prevent Neural Networks from Overfitting | 2014 | 正则化 |
| 020 | Adam: A Method for Stochastic Optimization | 2014 | 优化 |
| 021 | Layer Normalization | 2016 | 训练技巧 |
| 022 | Xception / Depthwise Separable Convolutions | 2016 | 视觉 |
| 023 | Neural Architecture Search with Reinforcement Learning | 2016 | AutoML |
| 024 | Weight Agnostic Neural Networks / lottery ticket 系列 | 2018+ | 理论 |
| 025 | GPT: Improving Language Understanding by Generative Pre-Training | 2018 | NLP |
| 026 | ELMo: Deep contextualized word representations | 2018 | NLP |
| 027 | GPT-2 / Language Models are Unsupervised Multitask Learners | 2019 | NLP |
| 028 | Denoising Diffusion Probabilistic Models (DDPM) | 2020 | 生成模型 |
| 029 | An Image is Worth 16x16 Words (ViT) | 2020 | 视觉 / Transformer |
| 030 | Learning Transferable Visual Models From Natural Language Supervision (CLIP) | 2021 | 多模态 |

</details>

## 推荐阅读方式

- **第一次读一篇**：每篇 PDF 按「原文与出处 → 逐段翻译 → 总结对照导读 + 我的理解」排列。先看开头确认论文坐标和 TL;DR，再读逐段对照（公式和表格保留原文），最后读结尾导读——那里才会告诉你哪些是核心创新、哪些是时代补丁；
- **带着问题读**：每篇导读都回答了"它之前的世界 → 它做了什么 → 它留下了什么"三个问题，读完后试着用自己的话复述一遍；
- **串起来读**：按清单顺序读，你会发现很多论文是在直接回应前一篇的缺陷（ResNet 回应深层退化、Transformer 回应 RNN 顺序瓶颈、BERT 把 Transformer 编码器推向预训练）；
- **不要逐字死磕**：工程细节（数据集、超参数表）第一遍可以略过，重点看"为什么这样设计"。

## 仓库结构

```
.
├── README.md      # 本文件：总览、选文标准、清单
├── *.pdf          # 每篇一个 PDF，文件名即论文名
└── LICENSE        # 署名-非商业性使用-相同方式共享 4.0
```

仓库只收录成品 PDF，不收录构建脚本与中间源文件。

## 关于翻译与版权

- 导读、译文与"我的理解"为原创内容，依据论文原文（优先使用作者公开的 LaTeX 源码）撰写；
- 论文原文、图表归原作者及其机构所有；本仓库的中文导读仅供学习研究使用，不构成对原文的替代；
- 如需引用论文，请引用 original paper；如需引用本导读，请注明本仓库地址。

## 反馈与贡献

发现翻译不准确、导读有误导、或想推荐"必读"论文？欢迎开 [Issue](https://github.com/EthanWang-cn/classic-papers-bilingual-guide/issues) 或直接提 PR。所有反馈都会认真看——这个仓库的目标是**真的帮人读懂论文**，不是凑数。

如果这份导读帮你省了时间，给个 ⭐ 让更多人看到。

---

<p align="center">持续更新中 · 目标 100 篇 · 每篇写完检查后单独提交</p>
