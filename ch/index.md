---
layout: about
title: 关于
permalink: /ch/
subtitle: <a href='#'>隶属</a> 西南大学. 更多信息请访问我的 [个人主页](https://vinyyang.github.io).

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false # crops the image to a circle
  more_info: >
    <div class="profile-info-header">
    <p>
    🏛️ 计算机与信息科学学院<br>
    🎓 西南大学<br>
    📍 中国重庆, 400715
    </p>
    </div>

selected_papers: true
social: true

announcements:
  enabled: true
  scrollable: true
  limit: 5

latest_posts:
  enabled: false
  scrollable: true
  limit: 3

lang: zh
---

<div class="stat-cards-container">
  <div class="stat-card stat-card-blue">
    <div class="stat-value">4.10/5.00</div>
    <div class="stat-label">GPA</div>
  </div>
  <div class="stat-card stat-card-pink">
    <div class="stat-value">2/123</div>
    <div class="stat-label">排名 前2%</div>
  </div>
  <div class="stat-card stat-card-cyan">
    <div class="stat-value">551</div>
    <div class="stat-label">CET-4</div>
  </div>
  <div class="stat-card stat-card-green">
    <div class="stat-value">570</div>
    <div class="stat-label">CET-6</div>
  </div>
</div>

<div id="content-zh" class="lang-content" markdown="1">

您好！我是**杨弘毅**，西南大学计算机科学与技术专业的本科生（2023-至今），成绩优异（GPA 4.10/5.00，排名 2/123），正以饱满的热情持续探索人工智能及其现实应用。

我的科研兴趣主要集中在**可视化**、**计算机视觉**和**大语言模型**。在校期间，我师从**[瞿经纬](https://jingweiqu.github.io/ch/index.html){:target="_blank"}**副教授，深入研究智能可视化生成。

针对传统标签引线生成方法存在的交叉重叠与审美缺失问题，我**独立**开展了"审美驱动的标签引导线生成"研究（第一作者，已投 **IEEE VIS**，CCF-A 会议）。我首次将引线生成建模为**马尔可夫决策过程 (MDP)**，利用深度强化学习（Maskable PPO）开发了智能体 **LeLA**；设计了包含空间拥挤度和潜在冲突特征的状态向量，并将"禁止交叉"、"斜线避让"等审美规则转化为分级成本函数。此外，我还设计了**风格统一算法**作为后处理，以提升视觉一致性。在 SWU-AMIL 数据集上，该方法使排列成本（AAC）降低了 **57.1%**，障碍物遮挡率降至 **0.57%**。用户研究表明，该方法生成的图表能显著降低认知负担，信息检索准确率达 **82.7%**。

此外，我正在开展**基于视觉语言模型（VLM）的 3D 注记布局评价**研究（2026年至今）。针对可视化/VR 领域中 3D 注记布局评价范式缺失，首次提出将 VLM 应用于该领域实现布局自动评价。基于 PartNet 数据集在 3D 场景下构建带有注记布局的数据集，并制定包含可读性、无歧义性、紧凑度、对齐度及审美的五维量化评价体系。通过知识蒸馏与 **LoRA** 微调实现高效部署，该方法实现了多种布局缺陷的量化评分。

我还参与了**基于 GAN 的布局注记剥离与背景重建**研究（2024-2025年）。开发了多任务**生成对抗网络（GAN）**架构，同步预测修复背景与注记掩码，引入加权损失函数优化对注记引导线等细微线性特征的捕捉。结合图像差分与线段检测自动化生成监督标签，并集成 OCR 与图论算法实现注记内容提取与理解。

在工程实践方面，我于大一期间在**重庆中科汽车软件创新中心**进行了实习，负责自动驾驶环境感知算法的研发与落地。基于 **mmsegmentation** 框架调研了 CCNet、DeepLabV3 等十余种模型，最终选定的 **CCNet** 在复杂路况下 mIoU 达到 44.54，并通过引入 Cityscapes 数据集联合训练解决了自采数据精度瓶颈。此外，利用 **NVIDIA IsaacSim** 搭建虚拟环境以弥合 Sim2Real 差距，并将训练好的模型与 **ROS** 系统交互，集成了基于雷达立体建模的 3D 目标检测（OpenPCDet），显著提升了实车的避障决策能力。

本科期间我有幸获得多个奖项，包括**国家奖学金**（2024年，2025年）、**西南大学三好学生**（2024，2025年）、**西南大学优秀学生干部**（2024年）、**全国大学生电子设计竞赛省级一等奖**（2025年）、**美国大学生数学建模竞赛 Finalist（特等奖提名）**（2025年）、**蓝桥杯国家级三等奖**（2025年），以及**国家发明专利**一项（2025年）。这些成就体现了我对理论理解和实际问题解决的执着追求。

**技术技能：** 熟悉 Python、C、C++，精通 R 和 LaTeX。拥有扎实的深度学习框架（PyTorch, mmseg）使用经验及嵌入式开发能力（ROS）。

欢迎浏览我的[学术主页](https://hongyiyoung.github.io)或访问我的[个人主页](https://vinyyang.github.io)了解更多关于我的项目和经历。非常欢迎通过[留言板](https://hongyiyang.online/guestbook)或其他展示的联系方式与我交流！

</div>
