---
layout: page
title: Autonomous Targeting Vision System
description: Computer vision system and hardware design 
img: assets/img/electronic_design_2025/cover.png
importance: 1
category: work
github: # Add your GitHub repository link here
tags: [Computer Vision, OpenMV, Embedded Systems, Real-time Processing]
---

## Overview

A comprehensive autonomous targeting system integrating **computer vision**, **embedded control**, and **precision mechanics**. This project demonstrates the application of classical computer vision algorithms with modern embedded platforms to achieve real-time target detection and trajectory control. Built upon my foundation in **STM32 development** (Keil5, HAL library) gained during freshman year and further enhanced through dedicated study, the system showcases practical implementation of multi-module communication protocols and perspective-adaptive algorithms.

**Technical Achievements:** Sub-centimeter targeting accuracy, real-time circle generation with <1/4 cycle synchronization error, and robust UART communication protocol with <30ms latency.

---

## System Demonstration

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="assets/video/electronic_design_2025/targeting_demo.mp4" class="img-fluid rounded z-depth-1" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include video.liquid path="assets/video/electronic_design_2025/circle_drawing.mp4" class="img-fluid rounded z-depth-1" controls=true %}
    </div>
</div>
<div class="caption">
    <strong>Left:</strong> Bullseye targeting demonstration | <strong>Right:</strong> 6cm radius circle drawing
</div>

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include video.liquid path="assets/video/electronic_design_2025/vision_system.mp4" class="img-fluid rounded z-depth-1" controls=true %}
    </div>
</div>
<div class="caption">
    Real-time vision processing pipeline demonstration
</div>

---

## Technical Architecture

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/electronic_design_2025/system_architecture.png" title="System Architecture" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    System architecture showing vision processing, main control, and motor control integration
</div>

### Hardware Selection & Comparison

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/electronic_design_2025/openmv_board.png" title="OpenMV H7" class="img-fluid rounded z-depth-1" %}
        <h6 class="mt-2 text-center"><strong>OpenMV H7</strong></h6>
        <p class="text-center small">✅ Rapid prototyping<br>✅ Compact size<br>✅ MicroPython</p>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/electronic_design_2025/k230_board.png" title="K230 Board" class="img-fluid rounded z-depth-1" %}
        <h6 class="mt-2 text-center"><strong>K230</strong></h6>
        <p class="text-center small">⚡ High AI performance<br>⚖️ Moderate size<br>🔧 Complex development</p>
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/electronic_design_2025/jetson_nano.png" title="Jetson Nano" class="img-fluid rounded z-depth-1" %}
        <h6 class="mt-2 text-center"><strong>Jetson Nano</strong></h6>
        <p class="text-center small">🚀 Mature ecosystem<br>❌ Large footprint<br>⏰ Long dev cycle</p>
    </div>
</div>
<div class="caption">
    Hardware comparison: OpenMV selected for optimal balance of development speed, size constraints, and task requirements
</div>

---

## Core Technologies

### 1. Perspective-Adaptive Target Detection
- **Classical Computer Vision**: Blob detection with multi-threshold filtering
- **Edge Boundary Checking**: Robust false-positive elimination
- **Diagonal Intersection Method**: Precise center calculation under perspective distortion

### 2. Real-time Circle Generation Algorithm
- **Perspective Compensation**: Dynamic ellipse parameter calculation
- **Synchronization Control**: Vehicle motion and drawing trajectory matching
- **Smooth Interpolation**: Angular velocity coordination for seamless operation

### 3. Multi-Module Communication Protocol
- **UART-based**: Custom frame protocol with error detection
- **Real-time Coordination**: <30ms latency between vision and control
- **Robust Data Transfer**: Frame validation and recovery mechanisms

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/electronic_design_2025/algorithm_flow.png" title="Vision Processing Pipeline" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Complete vision processing pipeline from target detection to coordinate output
</div>

---

## Performance Metrics

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Metric</th>
                    <th>Requirement</th>
                    <th>Achieved</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Targeting Accuracy</td>
                    <td>&lt; 2cm</td>
                    <td>&lt; 1.5cm</td>
                    <td><span class="badge badge-success">✓</span></td>
                </tr>
                <tr>
                    <td>Circle Radius Precision</td>
                    <td>6cm ± 0.5cm</td>
                    <td>6cm ± 0.3cm</td>
                    <td><span class="badge badge-success">✓</span></td>
                </tr>
                <tr>
                    <td>Synchronization Error</td>
                    <td>&lt; 1/2 cycle</td>
                    <td>&lt; 1/4 cycle</td>
                    <td><span class="badge badge-success">✓</span></td>
                </tr>
                <tr>
                    <td>Processing Latency</td>
                    <td>&lt; 50ms</td>
                    <td>&lt; 30ms</td>
                    <td><span class="badge badge-success">✓</span></td>
                </tr>
            </tbody>
        </table>
    </div>
</div>

---

## Implementation Details

### Vision Processing Module
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

### Communication Protocol
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

## Results & Recognition

{% include figure.liquid loading="eager" path="assets/img/electronic_design_2025/team_photo.png" title="Project Team" class="img-fluid rounded z-depth-1" %}

This project was successfully implemented and tested, achieving all target specifications. The system was later applied in the 2025 National College Student Electronic Design Contest, earning **Provincial First Prize**.

**Key Contributions:**
- Designed and implemented complete vision processing system
- Achieved sub-centimeter targeting accuracy under various conditions  
- Developed novel perspective-adaptive circle generation algorithm
- Established robust real-time communication between vision and control modules

---

## Technical Stack

<div class="row">
    <div class="col-sm-6">
        <h5>Hardware</h5>
        <ul>
            <li>OpenMV Cam H7 + Variable Focus Lens</li>
            <li>STM32 Main Controller (Keil5, HAL Library)</li>
            <li>MSPM0 Motor Controller</li>
            <li>High-precision Servo Motors</li>
        </ul>
    </div>
    <div class="col-sm-6">
        <h5>Software</h5>
        <ul>
            <li>MicroPython (OpenMV)</li>
            <li>Classical Computer Vision</li>
            <li>Real-time Control Algorithms</li>
            <li>Custom Communication Protocols</li>
        </ul>
    </div>
</div>

This project demonstrates the successful integration of **computer vision**, **embedded systems**, and **precision control** to solve complex real-world targeting challenges, showcasing practical application of theoretical knowledge in embedded system design.