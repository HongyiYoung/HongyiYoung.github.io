---
layout: about
title: about
permalink: /
subtitle: >
  <a href='#'>Undergraduate Student | Southwest University</a> | 
  <a href="#" onclick="switchLanguage('en'); return false;" style="text-decoration: none; color: #0066cc;">[English]</a> | 
  <a href="#" onclick="switchLanguage('zh'); return false;" style="text-decoration: none; color: #0066cc;">[中文]</a>

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false
  more_info: >
    <p style="font-weight: 600; font-family: 'SF Pro Display', 'Helvetica Neue', 'Arial', sans-serif; color: #333; margin: 0; line-height: 1.4;">
    🏛️ College of Computer and Information Science<br>
    🎓 Southwest University<br>
    📍 Chongqing, China
    </p>

selected_papers: true
social: true

announcements:
  enabled: true
  scrollable: true
  limit: 5

latest_posts:
  enabled: true
  scrollable: true
  limit: 3
---

<div style="display: flex; flex-wrap: wrap; gap: 15px; margin: 20px 0;">
  <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 15px; border-radius: 10px; text-align: center; min-width: 120px;">
    <div style="font-size: 24px; font-weight: bold;">3.0/5.0</div>
    <div style="font-size: 14px;">GPA</div>
  </div>
  <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 15px; border-radius: 10px; text-align: center; min-width: 120px;">
    <div style="font-size: 24px; font-weight: bold;">20/123</div>
    <div style="font-size: 10px; opacity: 0.8;">Top 10.63%</div>
    <div style="font-size: 14px;">Rank</div>
  </div>
  <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); color: white; padding: 15px; border-radius: 10px; text-align: center; min-width: 120px;">
    <div style="font-size: 24px; font-weight: bold;">451</div>
    <div style="font-size: 14px;">CET-4</div>
  </div>
  <div style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%); color: white; padding: 15px; border-radius: 10px; text-align: center; min-width: 120px;">
    <div style="font-size: 24px; font-weight: bold;">470</div>
    <div style="font-size: 14px;">CET-6</div>
  </div>
</div>

<div id="content-en" class="lang-content" markdown="1">

Hi there! I'm **Hongyi Yang**, a Computer Science and Technology undergraduate at Southwest University (2023-2027) with excellent academic performance. I'm passionate about exploring artificial intelligence and its real-world applications.

My research interests span **Computer Vision**, **Natural Language Processing**, **Embodied AI Systems** (such as autonomous driving, embodied AI, etc.), and other AI-related fields. During my internship at Chongqing Zhongke Automotive Software Innovation Center, I worked on 2D semantic segmentation and 3D object detection for autonomous driving scenarios, from dataset construction through IsaacSim simulation to real-vehicle deployment optimization, gaining comprehensive insights into autonomous driving systems.

During my undergraduate studies, I have been honored to receive multiple awards, including the **National Scholarship** (2024), **Provincial First Prize** in the National College Student Electronic Design Competition (2025), and **Finalist** in the Mathematical Contest in Modeling (MCM) (2025). These achievements reflect my dedication to both theoretical understanding and practical problem-solving.

**Technical Skills:** Proficient in Python, C, C++, and expert in R and LaTeX. Experienced with machine learning frameworks and embedded development, continuously advancing my expertise in autonomous systems and robotics.

Feel free to explore my [academic homepage](https://hongyiyoung.github.io) or visit my [personal homepage](https://vinyyang.github.io) to learn more about my projects and experiences. I warmly welcome communication through my [guestbook](https://hongyiyang.online/guestbook) or other contact methods displayed!

</div>

<div id="content-zh" class="lang-content" style="display: none;" markdown="1">

您好！我是**杨弘毅**，西南大学计算机科学与技术专业的本科生（2023-2027），成绩优异，正以饱满的热情持续探索人工智能及其现实应用。

我的研究兴趣涵盖**计算机视觉**、**自然语言处理**、**具身AI系统**（如自动驾驶、具身智能等）及其他与AI相关的工作。在重庆中科汽车软件创新中心实习期间，我从事自动驾驶场景下的2D语义分割、3D目标检测等工作，从数据集构建到借助IsaacSim仿真模拟再到实车部署优化，我对自动驾驶整个系统有了比较深入的认识。

本科期间我有幸获得多个奖项，包括**国家奖学金**（2024年）、**全国大学生电子设计竞赛省级一等奖**（2025年）和**美国大学生数学建模竞赛决赛入围奖**（2025年）。这些成就体现了我对理论理解和实际问题解决的执着追求。

**技术技能：** 熟悉Python、C、C++，精通R和LaTeX。有机器学习框架和嵌入式开发经验，在自主系统和机器人技术方面不断提升专业知识。

欢迎浏览我的[学术主页](https://hongyiyoung.github.io)或访问我的[个人主页](https://vinyyang.github.io)了解更多关于我的项目和经历。非常欢迎通过[留言板](https://hongyiyang.online/guestbook)或其他展示的联系方式与我交流！

</div>

<script>
function switchLanguage(lang) {
  var enContent = document.getElementById('content-en');
  var zhContent = document.getElementById('content-zh');
  
  if (lang === 'en') {
    enContent.style.display = 'block';
    zhContent.style.display = 'none';
  } else if (lang === 'zh') {
    enContent.style.display = 'none';
    zhContent.style.display = 'block';
  }
  
  // 阻止默认链接行为
  return false;
}

// 页面加载时检查URL hash
window.onload = function() {
  var hash = window.location.hash.substring(1);
  if (hash === 'zh') {
    switchLanguage('zh');
  } else {
    switchLanguage('en');
  }
};
</script>