---
layout: about
title: about
permalink: /
subtitle: <a href='#'>Affiliated with</a> Southwest University. More information can be seen on my [Personal Homepage](https://vinyyang.github.io).

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false
  more_info: >
    <div class="profile-info-card">
      <div class="profile-info-item">
        <span class="profile-info-icon">🏛️</span>
        <span>College of Computer and Information Science</span>
      </div>
      <div class="profile-info-item">
        <span class="profile-info-icon">🎓</span>
        <span>Southwest University</span>
      </div>
      <div class="profile-info-item">
        <span class="profile-info-icon">📍</span>
        <span>Chongqing, China</span>
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
---

<div class="stat-cards-container">
  <div class="stat-card stat-card-blue">
    <div class="stat-value">4.10/5.00</div>
    <div class="stat-label">GPA</div>
  </div>
  <div class="stat-card stat-card-pink">
    <div class="stat-value">2/123</div>
    <div class="stat-label">Rank Top 2%</div>
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

I'm **Hongyi Yang**, an undergraduate in Computer Science at Southwest University (2023–Present), supervised by Assoc. Prof. **[Jingwei Qu](https://jingweiqu.github.io/index.html){:target="_blank"}**. My research experience includes Multimodal Large Models, Computer Vision, Visualization, Virtual Reality, and Human-Computer Interaction. My research interests focus on Multimodal Large Models, Computer Vision, Agents, and Reinforcement Learning, with development experience in Multimodal Large Models, Computer Vision, and Embedded Development.

#### Research

1.**Aesthetics-Driven Leader Line Generation in Label Layouts** (2025.08–Present, 1st author, submitted to IEEE VIS, **CCF-A**)

In view management tasks, mainstream approaches primarily focus on label placement, neglecting the aesthetics of leader lines that serve as visual bridges. This work achieves leader line layout generation in complex scenarios by proposing a **Deep Reinforcement Learning**-based framework. We utilize the PPO algorithm for intelligent obstacle avoidance and dynamic generation of leader lines, while introducing a style-unified post-processing mechanism to ensure overall visual consistency. Experiments demonstrate that this method reduces the aesthetic cost of generated leader lines by 57.1% compared to baselines on the SWU-AMIL dataset, and it outperforms commercial layouts in user studies.

2.**VLM-based 3D Annotation Layout Evaluation** (2026.01–Present)

Addressing the lack of evaluation paradigms for 3D annotation layouts in the fields of Visualization and VR, we propose the first application of **VLMs** for automated layout assessment in this domain. Based on the PartNet dataset, we construct an annotated layout dataset in 3D scenes, develop a multi-dimensional quantitative evaluation framework encompassing readability and unambiguity, and utilize knowledge distillation to generate a structured scoring dataset. By fine-tuning a lightweight model via **LoRA** for efficient deployment, this method achieves precise identification and quantitative scoring of layout defects (e.g., label occlusion, leader line intersection). It provides an efficient and objective automated evaluation tool for annotation layouts in complex 3D scenes.

3.**GAN-based Annotation Stripping and Background Reconstruction** (2024.12–2025.07)

Addressing the challenge of stripping annotations from images, we employ a **GAN** to simultaneously predict the annotation mask and reconstruct the background. A weighted loss function is introduced to optimize the capture of fine linear features such as annotation leader lines, thereby resolving the high-fidelity restoration of underlying device details in complex backgrounds. By combining image differencing and line segment detection, we automatically generate the supervision labels required for model training, and integrate OCR and graph theory algorithms to extract and comprehend the annotation content. This approach achieves accurate stripping of complex annotations and background reconstruction, significantly improving the construction efficiency of structured image datasets.

#### Awards

1.**Honorary Awards**: National Scholarship (2024, 2025), Merit Student of SWU (2024, 2025), Outstanding Student Cadre of SWU (2024)

2.**Competition Awards**: MCM Finalist (2025), National Undergraduate Electronics Design Contest Provincial 1st Prize (2025), Lanqiao Cup National Software and Information Technology Professionals Competition National 3rd Prize (2025), National Invention Patent (1st author) (2025), etc.

#### Internship

**Chongqing Zhongke Automotive Software Innovation Center** (2024): Autonomous Driving Vision Algorithm Intern. Fully completed the pipeline from image collection, labeling, and dataset organization to model training and comparison. Benchmarked 10+ semantic segmentation models and deployed CCNet (mIoU 44.54) on campus autonomous vehicles. Combined NVIDIA IsaacSim simulation with 3D object detection to further enhance the vehicle's intelligent obstacle avoidance capabilities.

#### Skills

Python, C/C++, R, LaTeX, PyTorch, Visio, STM32, OpenMV embedded development, etc.
