---
layout: page
title: 自主瞄准视觉系统
description: 计算机视觉系统与硬件设计
img: assets/img/electronic_design_2025/cover.png
importance: 1
category: work
lang: zh
github: # Add your GitHub repository link here
tags: [计算机视觉, OpenMV, 嵌入式系统, 实时处理]
---

## 概览

这是一个集成了**计算机视觉**、**嵌入式控制**和**精密机械**的综合性自主瞄准系统。该项目展示了经典计算机视觉算法与现代嵌入式平台的结合，实现了实时的目标检测和轨迹控制。基于我在大一期间获得的 **STM32 开发**（Keil5, HAL 库）基础，并通过进一步的深入学习，该系统展示了多模块通信协议和透视自适应算法的实际应用。

**主要技术成果：** 实现了亚厘米级的瞄准精度，误差小于 1/4 周期的实时画圆生成，以及延迟低于 30ms 的鲁棒 UART 通信协议。

---

## 系统演示

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="assets/video/electronic_design_2025/targeting_demo.mp4" class="img-fluid rounded z-depth-1" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="assets/video/electronic_design_2025/circle_drawing.mp4" class="img-fluid rounded z-depth-1" controls=true %}
    </div>
</div>
<div class="caption">
    <strong>左：</strong> 靶心瞄准演示 | <strong>右：</strong> 6cm 半径画圆演示
</div>

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include video.liquid path="assets/video/electronic_design_2025/vision_system.mp4" class="img-fluid rounded z-depth-1" controls=true %}
    </div>
</div>
<div class="caption">
    实时视觉处理流程演示
</div>

---

## 技术架构

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/electronic_design_2025/system_architecture.png" title="System Architecture" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    展示视觉处理、主控和电机控制集成的系统架构
</div>

### 硬件选型与对比

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/electronic_design_2025/openmv_board.png" title="OpenMV H7" class="img-fluid rounded z-depth-1" %}
        <h6 class="mt-2 text-center"><strong>OpenMV H7</strong></h6>
        <p class="text-center small">✅ 快速原型开发<br>✅ 体积小巧<br>✅ MicroPython</p>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/electronic_design_2025/k230_board.png" title="K230 Board" class="img-fluid rounded z-depth-1" %}
        <h6 class="mt-2 text-center"><strong>K230</strong></h6>
        <p class="text-center small">⚡ 高 AI 性能<br>⚖️ 尺寸适中<br>🔧 开发复杂</p>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/electronic_design_2025/jetson_nano.png" title="Jetson Nano" class="img-fluid rounded z-depth-1" %}
        <h6 class="mt-2 text-center"><strong>Jetson Nano</strong></h6>
        <p class="text-center small">🚀 成熟生态系统<br>❌ 占用空间大<br>⏰ 开发周期长</p>
    </div>
</div>
<div class="caption">
    硬件对比：选择 OpenMV 以平衡开发速度、尺寸限制和任务需求
</div>

---

## 核心技术

### 1. 透视自适应目标检测

- **经典计算机视觉**：基于多阈值过滤的斑点检测
- **边缘边界检查**：鲁棒的误检消除
- **对角线交点法**：透视畸变下的精确中心计算

### 2. 实时画圆算法

- **透视补偿**：动态椭圆参数计算
- **同步控制**：车辆运动与绘制轨迹匹配
- **平滑插值**：角速度协调以实现无缝操作

### 3. 多模块通信协议

- **基于 UART**：带错误检测的自定义帧协议
- **实时协调**：视觉与控制之间的延迟 <30ms
- **鲁棒数据传输**：帧验证与恢复机制

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/electronic_design_2025/algorithm_flow.png" title="Vision Processing Pipeline" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    从目标检测到坐标输出的完整视觉处理流程
</div>

---

## 性能指标

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>指标</th>
                    <th>要求</th>
                    <th>实现</th>
                    <th>状态</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>瞄准精度</td>
                    <td>&lt; 2cm</td>
                    <td>&lt; 1.5cm</td>
                    <td><span class="badge badge-success">✓</span></td>
                </tr>
                <tr>
                    <td>画圆半径精度</td>
                    <td>6cm ± 0.5cm</td>
                    <td>6cm ± 0.3cm</td>
                    <td><span class="badge badge-success">✓</span></td>
                </tr>
                <tr>
                    <td>同步误差</td>
                    <td>&lt; 1/2 周期</td>
                    <td>&lt; 1/4 周期</td>
                    <td><span class="badge badge-success">✓</span></td>
                </tr>
                <tr>
                    <td>处理延迟</td>
                    <td>&lt; 50ms</td>
                    <td>&lt; 30ms</td>
                    <td><span class="badge badge-success">✓</span></td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

---

## 实现细节

### 视觉处理模块

```python
# Core blob detection with multi-criteria filtering
def find_target_boundary_rect(img):
    blobs = img.find_blobs([BLACK_THRESHOLD],
                          pixels_threshold=min_pixels,
                          area_threshold=min_area)

    # Edge boundary validation
    valid_blobs = filter_edge_touching_blobs(blobs)

    # Perspective center calculation
    return calculate_diagonal_intersection(valid_blobs)
```

### 通信协议

```python
# Custom UART frame structure
def send_coordinates(x, y):
    frame = struct.pack('<BBBBBB',
                       0x3C, 0x3B,    # Header
                       x, y,          # Coordinates
                       0x01, 0x01)    # Footer
    uart.write(frame)
```

---

## 结果与荣誉

{% include figure.liquid loading="eager" path="assets/img/electronic_design_2025/team_photo.png" title="Project Team" class="img-fluid rounded z-depth-1" %}

该项目已成功实施并测试，达到了所有目标规格。该系统随后应用于 **2025 年全国大学生电子设计竞赛**，荣获 **省部级一等奖**。

**主要贡献：**

- 设计并实现了完整的视觉处理系统
- 在各种条件下实现了亚厘米级的瞄准精度
- 开发了新颖的透视自适应画圆算法
- 建立了视觉与控制模块之间鲁棒的实时通信

---

## 技术栈

<div class="row">
    <div class="col-sm-6">
        <h5>硬件</h5>
        <ul>
            <li>OpenMV Cam H7 + 变焦镜头</li>
            <li>STM32 主控制器 (Keil5, HAL 库)</li>
            <li>MSPM0 电机控制器</li>
            <li>高精度伺服电机</li>
        </ul>
    </div>
    <div class="col-sm-6">
        <h5>软件</h5>
        <ul>
            <li>MicroPython (OpenMV)</li>
            <li>经典计算机视觉</li>
            <li>实时控制算法</li>
            <li>自定义通信协议</li>
        </ul>
    </div>
</div>

该项目展示了 **计算机视觉**、**嵌入式系统** 和 **精密控制** 的成功集成，解决了复杂的现实世界瞄准挑战，展示了理论知识在嵌入式系统设计中的实际应用。
