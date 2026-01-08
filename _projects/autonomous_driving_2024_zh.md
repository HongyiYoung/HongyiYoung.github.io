---
layout: page
title: 自动驾驶感知系统
description: 基于深度学习的智能车辆 2D 语义分割与 3D 目标检测
img: assets/img/autonomous_driving_2024/cover.png
importance: 2
category: work
lang: zh
github: # Add your GitHub repository link here
tags: [计算机视觉, 深度学习, 自动驾驶, 语义分割, 3D目标检测]
---

## 项目概览

这是一个集成了先进 **2D 语义分割** 和 **3D 目标检测** 算法的综合性 **自动驾驶感知系统**。该项目是我在 **重庆中科汽车软件创新中心** 实习期间完成的，专注于智能车辆的核心感知技术。系统展示了从数据集构建、**IsaacSim 仿真** 到 **实车部署** 的完整流程，体现了前沿深度学习算法在自动驾驶场景中的落地应用。

**主要技术成果：** 实现了像素级精度的实时语义分割，在多种天气条件下鲁棒的 3D 目标检测，以及使用 **MMSegmentation** 和 **MMDetection3D** 框架构建的从仿真到实车测试的完整验证体系。

---

## 系统演示

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="assets/video/autonomous_driving_2024/real_vehicle_semantic_1.mp4" class="img-fluid rounded z-depth-1" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="assets/video/autonomous_driving_2024/real_vehicle_semantic_2.mp4" class="img-fluid rounded z-depth-1" controls=true %}
    </div>
</div>
<div class="caption">
    <strong>左：</strong> 实车 2D 语义分割演示 | <strong>右：</strong> 额外测试场景
</div>

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include video.liquid path="assets/video/autonomous_driving_2024/isaac_sim_validation.mp4" class="img-fluid rounded z-depth-1" controls=true %}
    </div>
</div>
<div class="caption">
    用于算法验证和参数优化的 IsaacSim 仿真环境
</div>

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include video.liquid path="assets/video/autonomous_driving_2024/3d_detection_demo.mp4" class="img-fluid rounded z-depth-1" controls=true %}
    </div>
</div>
<div class="caption">
    展示空间定位和多目标跟踪能力的 3D 目标检测演示
</div>

---

## 技术架构

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/autonomous_driving_2024/segmentation_pipeline.png" title="Semantic Segmentation Pipeline" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    从数据输入到最终预测的完整语义分割处理流程
</div>

### 技术栈概览

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/autonomous_driving_2024/semantic_segmentation.png" title="2D Semantic Segmentation" class="img-fluid rounded z-depth-1" %}
        <h6 class="mt-2 text-center"><strong>2D 语义分割</strong></h6>
        <p class="text-center small">🎯 像素级理解<br>🚗 道路场景解析<br>⚡ 实时处理</p>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/autonomous_driving_2024/3d_detection.png" title="3D Object Detection" class="img-fluid rounded z-depth-1" %}
        <h6 class="mt-2 text-center"><strong>3D 目标检测</strong></h6>
        <p class="text-center small">📏 空间定位<br>🎯 多类别检测<br>📊 距离估计</p>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/autonomous_driving_2024/isaac_sim.png" title="IsaacSim Platform" class="img-fluid rounded z-depth-1" %}
        <h6 class="mt-2 text-center"><strong>IsaacSim 验证</strong></h6>
        <p class="text-center small">🌐 虚拟测试<br>🔄 参数调优<br>✅ 安全验证</p>
    </div>
</div>
<div class="caption">
    多模态感知方案：2D 理解 + 3D 空间感知 + 仿真验证
</div>

---

## 核心技术

### 1. 先进 2D 语义分割

**框架集成：** 基于 **MMSegmentation** 构建，利用了针对车载场景优化的 PSPNet、DeepLabV3+ 和 Swin Transformer 等最先进的分割算法。

语义分割模块对 19 个不同的语义类别（包括道路边界、车辆、行人、交通标志和可行驶区域）进行像素级场景理解。该实现利用了专门针对汽车应用优化的深度学习架构，确保了准确性和计算效率。模型量化和 TensorRT 优化技术使其能够在 NVIDIA Xavier 平台上实时部署，同时保持高质量的分割效果。

### 2. 3D 目标检测集成

**框架集成：** 使用 **MMDetection3D** 和点云处理技术实现，3D 目标检测组件通过提供空间感知能力补充了 2D 语义分割系统。

3D 检测系统处理激光雷达点云数据，实现周围物体的空间定位。该实现采用了多模态融合技术，结合摄像头 RGB 数据和激光雷达点云，提高了整体感知精度。

### 3. 仿真到现实（Sim-to-Reality）流水线

项目建立了一个综合验证框架，通过先进的域适应技术弥合仿真与现实部署之间的差距。NVIDIA IsaacSim 提供了一个具有精确物理建模的照片级写实仿真环境，使得算法在实车部署前能在安全的虚拟环境中进行广泛测试。

---

## 性能指标与验证

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/autonomous_driving_2024/model_comparison.png" title="Model Performance Comparison" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    包括 UNet、CCNet 和其他先进架构在内的多种 MMSegmentation 模型性能对比
</div>

---

## 数据集构建与训练

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/autonomous_driving_2024/annotation_tool.png" title="Data Annotation Process" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    用于像素级语义标注和质量控制的专业标注工具界面
</div>

---

## 实车部署与测试

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/autonomous_driving_2024/vehicle_setup.png" title="Real Vehicle Testing Setup" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    测试车辆上的完整传感器设置，包括同步摄像头阵列和激光雷达系统
</div>

这是一个将深度学习、计算机视觉和自动驾驶系统应用于解决智能车辆实际感知挑战的成功案例。
