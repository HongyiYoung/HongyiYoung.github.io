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
    <div class="profile-info-header">
    <p>
    🏛️ College of Computer and Information Science<br>
    🎓 Southwest University<br>
    📍 Chongqing, China
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


Hi there! I'm **Hongyi Yang**, an undergraduate student majoring in **Computer Science and Technology** at Southwest University (2023-Present). I maintain excellent academic performance (GPA 4.10/5.00, Rank 2/123) and am passionately exploring Artificial Intelligence and its real-world applications.

My research journey focuses on **Visualization** and **AI**, under the supervision of Associate Professor **[Jingwei Qu](https://jingweiqu.github.io/index.html){:target="_blank"}** (Qu Jingwei). 

In the field of visualization, addressing the visual clutter and crossings in traditional leader-line generation, I **independently** proposed a novel **Aesthetic-Driven Leader Line Generation** framework (first author, submitted to **IEEE VIS**, CCF-A). I modeled the generation process as a **Markov Decision Process (MDP)** and developed a **Leader-Line Agent (LeLA)** using **Maskable PPO** (Deep Reinforcement Learning). By designing comprehensive state vectors (congestion, conflict risk) and translating complex aesthetic rules into cost functions, combined with a **Style Unification Algorithm** for refinement, my model effectively minimizes crossings. Experiments on the SWU-AMIL dataset showed a **57.1% reduction in Aesthetic Arrangement Cost** and a drop in occlusion rate to **0.57%**. User studies further confirmed that my method significantly lowers mental load and improves information retrieval accuracy (**82.7%**).

Additionally, I am conducting research on **VLM-based 3D Annotation Layout Evaluation** (2026-Present). Addressing the lack of evaluation paradigms for 3D annotation layouts in visualization and VR, I first proposed applying **Vision-Language Models (VLM)** for automated layout assessment. Based on the PartNet dataset, I constructed annotated layout datasets in 3D scenes and established a five-dimensional quantitative evaluation framework covering readability, unambiguity, compactness, alignment, and aesthetics. Using knowledge distillation and **LoRA** fine-tuning for efficient deployment, this method enables precise identification and quantitative scoring of various layout defects.

I also worked on **GAN-based Annotation Stripping and Background Reconstruction** (2024-2025). I developed a multi-task **Generative Adversarial Network (GAN)** architecture that simultaneously predicts repaired backgrounds and annotation masks, with weighted loss functions optimized for capturing fine linear features such as leader lines. Combined with image differencing and line segment detection for automated supervision label generation, and integrated OCR with graph algorithms for annotation content extraction and understanding.

On the engineering side, I gained comprehensive insights into **Embodied AI Systems** during my internship at **Chongqing Zhongke Automotive Software Innovation Center** (Freshman Year). I led the development of environment perception algorithms for autonomous driving, aiming to enhance obstacle avoidance. I managed the high-precision pixel-level annotation of self-collected datasets using **PixelAnnotation Tool** and benchmarked 10+ mainstream segmentation models on **mmsegmentation**, identifying **CCNet** as the optimal solution (mIoU 44.54). To bridge the Sim2Real gap, I leveraged **NVIDIA IsaacSim** for simulation and deployed the system on **ROS** inclusive of 3D object detection (OpenPCDet), achieving real-time visualization via multi-machine communication.

I have been honored to receive multiple awards, including the **National Scholarship** (2024, 2025), **Merit Student of SWU** (2024, 2025), **Outstanding Student Cadre of SWU** (2024), **Provincial First Prize** in the National Undergraduate Electronics Design Contest (2025), **Finalist** in the Mathematical Contest in Modeling (MCM/ICM) (2025), **National Third Prize** in the Blue Bridge Cup (2025), and one **National Invention Patent** (2025). These achievements demonstrate my commitment to both theoretical depth and practical problem-solving.

**Technical Skills:** Proficient in Python, C, C++, R, and LaTeX. Experienced in deep learning frameworks (PyTorch, mmsegmentation) and embedded development (ROS).

Feel free to explore my [academic homepage](https://hongyiyoung.github.io) or visit my [personal homepage](https://vinyyang.github.io) to learn more about my projects and experiences. I warmly welcome communication through my [guestbook](https://hongyiyang.online/guestbook) or other contact methods displayed!