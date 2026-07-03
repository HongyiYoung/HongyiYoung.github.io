---
layout: about
title: 关于
permalink: /ch/
subtitle: <a href='#'>隶属</a> 西南大学. 更多信息请访问我的 [个人主页](https://vinyyang.github.io).

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false
  more_info: >
    <div class="profile-info-card">
      <div class="profile-info-item">
        <span class="profile-info-icon">🏛️</span>
        <span>计算机与信息科学学院</span>
      </div>
      <div class="profile-info-item">
        <span class="profile-info-icon">🎓</span>
        <span>西南大学</span>
      </div>
      <div class="profile-info-item">
        <span class="profile-info-icon">📍</span>
        <span>中国重庆, 400715</span>
      </div>
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
    <div class="stat-value stat-value-wide">4.10/5.00</div>
    <div class="stat-label">GPA</div>
  </div>
  <div class="stat-card stat-card-pink">
    <div class="stat-value">2/123</div>
    <div class="stat-label">排名前 2%</div>
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

我是**杨弘毅**，西南大学计算机科学与技术专业本科生（2023–至今），师从**[瞿经纬](https://jingweiqu.github.io/ch/index.html){:target="_blank"}**副教授。研究经历为多模态大模型、计算机视觉、可视化、虚拟现实与人机交互，研究兴趣为多模态大模型、计算机视觉、智能体、强化学习等，有多模态大模型、计算机视觉、嵌入式等开发经验。

#### 科研经历

**1.基于 DRL 的标签布局引导线生成**（2025.08–至今，第一作者在投 IEEE VIS，**CCF-A**）

视图管理任务中，主流方法主要关注标签放置，而清晰且无碰撞的引导线生成仍未被充分探索。本工作实现复杂场景下引导线布局生成，提出一种基于**深度强化学习**的引导线生成框架。利用 PPO 算法实现了引导线的智能避障与动态生成，并引入风格统一的后处理机制确保整体布局的视觉一致性。实验表明，该方法在 SWU-AMIL 数据集上较基线提升布局清晰度 5.71%，文本标签遮挡率仅为 0.07%，且用户研究中表现优于商用布局。

**2.基于 MLLM 的 3D 注记布局评价**（2026.01–至今）

针对可视化与 VR 领域中 3D 注记布局评价范式缺失，首次提出将**多模态大语言模型（MLLM）**应用于该领域实现布局自动评价。基于 PartNet 数据集在 3D 场景下构建带有注记布局的数据集，并制定包含可读性、无歧义性等多维量化评价体系，利用知识蒸馏生成结构化评分数据集。通过 **LoRA** 技术对轻量化模型进行微调以实现高效部署；该方法实现了对标签遮挡、引导线交叉等多种布局缺陷的精准识别与量化评分，为复杂 3D 场景下的注记布局提供了高效、客观的自动化评估手段。

**3.基于 GAN 的布局注记剥离与背景重建**（2024.12–2025.07）

针对带有注记布局图片的注记剥离难题，基于 **GAN** 同步预测修复背景与注记掩码，同时引入加权损失函数优化对注记引导线等细微线性特征的捕捉，解决了复杂背景下装置底层细节的高保真修复问题；结合图像差分与线段检测自动化生成模型训练所需的监督标签，并集成 OCR 与图论算法实现注记内容的提取与理解。该方法实现了复杂注记的精准剥离与背景重建，显著提升了结构化图像数据集的构建效率。

#### 获奖情况

**1.荣誉奖项：**国家奖学金（2024, 2025）、西南大学三好学生（2024, 2025）、西南大学优秀学生干部（2024）

**2.竞赛奖项：**美国大学生数学建模竞赛特等奖提名（2025）、全国大学生电子设计竞赛省部级一等奖（2025）、蓝桥杯全国软件和信息技术专业人才大赛国家级三等奖（2025）、国家发明专利（第一作者）（2025）等

#### 实习经历

**重庆中科汽车软件创新中心**（2024）：自动驾驶视觉算法实习生。完整完成从图片采集、打标、数据集整理、模型训练与对比的全过程，评估 10+语义分割模型，在园区小车中部署 CCNet（mIoU 44.54），结合 NVIDIA IsaacSim 仿真与 3D 目标检测进一步提升小车智能避障能力。

#### 技术技能

Python, C/C++, R, LaTeX , PyTorch, Visio, STM32, OpenMV 嵌入式开发等

</div>
