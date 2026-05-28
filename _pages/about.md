---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am a master's student at FudanNLP Lab, Fudan University. My research focuses on **autonomous agents** and **reinforcement learning**, with current interests in agent memory and long-horizon context management. I am currently an Algorithm Researcher at NEX-AGI (Shanghai Qiji Zhifeng Co., Ltd.), and previously interned at the Computing Research Department of Huawei. I received my B.S. from Fudan University in 2024.

You can find my publications on <a href='https://scholar.google.com/citations?user=bn6dnQ8AAAAJ'>Google Scholar <strong><span id='total_cit'></span></strong></a> <a href='https://scholar.google.com/citations?user=bn6dnQ8AAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.


# 🔥 News
- Stay tuned…

# 🎯 Research Interests
- Autonomous Agents
- Reinforcement Learning
- Agent Memory and Context Management

# 💻 Internships
- *2025.03 - Present*, Algorithm Researcher, **NEX-AGI** (Shanghai Qiji Zhifeng Co., Ltd.), Shanghai. Working on agent memory and context management.
- *2024.07 - 2024.09*, Research Intern, **Huawei**, Computing Product Line, Computing Research Department.

# 📝 Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv 2026</div><img src='../images/agentic-harness-engineering-training-curve.webp' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

### Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses

**Jiahang Lin**\*, Shichun Liu\*, Chengjun Pan\*, Lizhi Lin, Shihan Dou, Xuanjing Huang, Hang Yan, Zhenhua Han<small>†</small>, Tao Gui<small>†</small>

- AHE is an observability stack for the automatic optimization of coding-agent harnesses, with three pillars: component observability (NexAU), experience observability (Agent Debugger), and decision observability (evidence-driven Evolve Agent).
- Without changing the model, AHE pushes Terminal-bench 2 from 69.7% to 77.0% across iterations, with strong cross-task and cross-model generalization.
- [![](https://img.shields.io/badge/Paper-fff?logo=readthedocs&logoColor=000)](https://arxiv.org/abs/2604.25850) \| [![](https://img.shields.io/badge/Code-fff?logo=github&logoColor=000)](https://github.com/china-qijizhifeng/agentic-harness-engineering)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv 2026</div><img src='../images/evpo-overview.webp' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

### EVPO: Explained Variance Policy Optimization for Adaptive Critic Utilization in LLM Post-Training

Chengjun Pan\*, Shichun Liu\*, **Jiahang Lin**\*, Dingwei Zhu, Jiazheng Zhang, Shihan Dou, Songyang Gao, Zhenhua Han, Binghai Wang, Rui Zheng, Xuanjing Huang<small>†</small>, Tao Gui<small>†</small>, Yansong Feng<small>†</small>

- We cast baseline selection in LLM post-training as a Kalman filtering problem, unifying PPO and GRPO as two extremes of the Kalman gain, and prove that the sign of explained variance (EV) is the exact boundary separating the variance-reducing from the variance-inflating critic regime.
- EVPO adaptively switches between critic-based and batch-mean advantage estimation per step based on EV sign, achieving the best results across Sokoban, FrozenLake, WebShop, and MATH.
- [![](https://img.shields.io/badge/Paper-fff?logo=readthedocs&logoColor=000)](https://arxiv.org/abs/2604.19485)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv 2026</div><img src='../images/500x300.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

### MM-Doc-R1: Training Agents for Long Document Visual Question Answering through Multi-turn Reinforcement Learning

**Jiahang Lin**, Kai Hu, Binghai Wang, Yuhao Zhou, Zhiheng Xi, Honglin Guo, Shichun Liu, Junzhe Wang, Shihan Dou, Enyu Zhou, Hang Yan, Zhenhua Han, Tao Gui<small>†</small>, Qi Zhang<small>†</small>, Xuanjing Huang<small>†</small>

- Conventional RAG systems struggle with complex multi-hop queries over long documents due to their single-pass retrieval. MM-Doc-R1 trains agents for long-document visual question answering via multi-turn reinforcement learning.
- The agent learns to interleave retrieval and reasoning across many turns, achieving substantial gains on long-document VQA benchmarks compared to single-pass and prompt-only baselines.
- [![](https://img.shields.io/badge/Paper-fff?logo=readthedocs&logoColor=000)](https://arxiv.org/abs/2604.13579)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv 2026</div><img src='../images/octobench.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

### OctoBench: Benchmarking Scaffold-Aware Instruction Following in Repository-Grounded Agentic Coding

Deming Ding\*, Shichun Liu\*, Enhui Yang\*, **Jiahang Lin**\*, Ziying Chen, Shihan Dou, Honglin Guo, Weiyu Cheng, Pengyu Zhao, Chengjun Xiao, Qunhong Zeng, Qi Zhang, Xuanjing Huang, Qidi Xu, Tao Gui

- Modern coding scaffolds turn LLMs into capable software agents, but their ability to follow scaffold-specified instructions remains under-examined. OctoBench benchmarks scaffold-aware instruction following in repository-grounded agentic coding.
- OctoBench includes 34 environments and 217 tasks under three scaffold types, with 7,098 objective checklist items. We release an automated observation-and-scoring toolkit for full trajectories and fine-grained checks.
- [![](https://img.shields.io/badge/Paper-fff?logo=readthedocs&logoColor=000)](https://arxiv.org/abs/2601.10343)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv 2025</div><img src='../images/nex-n1.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

### Nex-N1: Agentic Models Trained via a Unified Ecosystem for Large-Scale Environment Construction

Nex-AGI Team: Yuxuan Cai, Lu Chen, …, **Jiahang Lin**, …, Xuanjing Huang, Xipeng Qiu

- We introduce a comprehensive method designed to systematically scale the diversity and complexity of interactive environments through three orthogonal dimensions: Complexity (NexAU), Diversity (NexA4A), and Fidelity (NexGAP).
- Nex-N1 consistently outperforms SOTA open-source models and achieves competitive performance against frontier proprietary models on complex agentic tasks (SWE-bench, tau2).
- [![](https://img.shields.io/badge/Paper-fff?logo=readthedocs&logoColor=000)](https://arxiv.org/abs/2512.04987)

</div>
</div>

# 🎖 Honors and Awards
- *2024*, **1st Prize**, Tencent Open AI Competition · Agent Game Algorithm Track · Mainland China Regional Final. Team: 五角场三分王, Fudan University.

# 📖 Education
- *2024.09 - Present*, **M.S.**, Fudan University (FudanNLP Lab).
- *2020.09 - 2024.06*, **B.S.**, Fudan University.
