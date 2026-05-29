---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<span class='anchor' id='about-me'></span>

I am a master's student at FudanNLP Lab, Fudan University. My research focuses on **self-evoling agents** and **reinforcement learning**. I have end-to-end experience across the agent post-training stack — SFT (DeepSpeed, LLaMA-Factory), RL (verl, trl), and harness engineering. I am currently an Algorithm Researcher at NEX-AGI (Shanghai Qiji Zhifeng Co., Ltd.), and previously interned at the Computing Research Department of Huawei. I received my B.S. from Fudan University in 2024.

You can find my publications on <a href='https://scholar.google.com/citations?user=bn6dnQ8AAAAJ'>Google Scholar</a>.

[![Total GitHub Stars](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FCurry09%2FCurry09.github.io%2Fstar-badge%2Ftotal-stars.json)](https://github.com/Curry09)

# 🔥 News
- Stay tuned…

# 🎯 Research Interests
- Self-evoling Agents
- Reinforcement Learning

# 💻 Internships
- <span style="display: inline-flex; align-items: center; justify-content: center; width: 160px; height: 75px; vertical-align: middle; margin-right: 10px;"><img src="../images/NEX.svg" alt="NEX-AGI" style="max-width: 160px; max-height: 50px;"></span><span style="display: inline-block; vertical-align: middle;">**2025.3 - Present** · Algorithm Researcher, **NEX-AGI** (Shanghai Qiji Zhifeng Co., Ltd.), Shanghai</span><br>Self-evolving agents & reinforcement learning for coding and search agents
- <span style="display: inline-flex; align-items: center; justify-content: center; width: 160px; height: 75px; vertical-align: middle; margin-right: 10px;"><img src="../images/huawei.svg" alt="Huawei" style="max-width: 160px; max-height: 50px;"></span><span style="display: inline-block; vertical-align: middle;">**2024.7 - 2024.9** · Research Intern, **Huawei** Computing Product Line, Computing Research Department</span><br>Fine-tuning long-context LLMs on Ascend 910B
- <span style="display: inline-flex; align-items: center; justify-content: center; width: 160px; height: 75px; vertical-align: middle; margin-right: 10px;"><img src="../images/fudannlp.png" alt="FudanNLP" style="max-width: 160px; max-height: 50px;"></span><br><span style="display: inline-block; vertical-align: middle;">**2024.4 - 2024.7** · Research Intern, **FudanNLP Lab**, Fudan University</span><br>LLM safety: training red-team models for attack and defense

# 📝 Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv 2026</div><img src='../images/agentic-harness-engineering-training-curve.webp' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

### Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses

**Jiahang Lin**\*, Shichun Liu\*, Chengjun Pan\*, Lizhi Lin, Shihan Dou, Xuanjing Huang, Hang Yan, Zhenhua Han<small>†</small>, Tao Gui<small>†</small>

- AHE is an observability stack for the automatic optimization of coding-agent harnesses, with three pillars: component observability (NexAU), experience observability (Agent Debugger), and decision observability (evidence-driven Evolve Agent).
- Without changing the model, AHE pushes Terminal-bench 2 from 69.7% to 77.0% across iterations, with strong cross-task and cross-model generalization.
- [![](https://img.shields.io/badge/Paper-fff?logo=readthedocs&logoColor=000)](https://arxiv.org/abs/2604.25850) \| [![](https://img.shields.io/badge/Code-fff?logo=github&logoColor=000)](https://github.com/china-qijizhifeng/agentic-harness-engineering) \| [![](https://img.shields.io/github/stars/china-qijizhifeng/agentic-harness-engineering?style=social)](https://github.com/china-qijizhifeng/agentic-harness-engineering)

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


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv 2026</div><img src='../images/mm-doc-r1.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

### MM-Doc-R1: Training Agents for Long Document Visual Question Answering through Multi-turn Reinforcement Learning

**Jiahang Lin**\*, Kai Hu\*, Binghai Wang, Yuhao Zhou, Zhiheng Xi, Honglin Guo, Shichun Liu, Junzhe Wang, Shihan Dou, Enyu Zhou, Hang Yan, Zhenhua Han, Tao Gui<small>†</small>, Qi Zhang<small>†</small>, Xuanjing Huang<small>†</small>

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
- [![](https://img.shields.io/badge/Paper-fff?logo=readthedocs&logoColor=000)](https://arxiv.org/abs/2512.04987) \| [![](https://img.shields.io/github/stars/nex-agi/Nex-N1?style=social)](https://github.com/nex-agi/Nex-N1)

</div>
</div>

# 🎖 Honors and Awards
- *2024*, **1st Prize**, Tencent Open AI Competition · Agent Game Algorithm Track · Mainland China Regional Final. Team: 五角场三分王, Fudan University.

# 📖 Education
- *2025.09 - Present*, **M.S.**, Fudan University (FudanNLP Lab).
- *2021.09 - 2025.06*, **B.S.**, Fudan University.
