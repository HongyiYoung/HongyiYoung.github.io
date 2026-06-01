# 学术主页 (Academic Homepage)

基于 Jekyll 和 [al-folio](https://github.com/alshedivat/al-folio) 主题构建的简洁、美观且响应式的学术主页。

## 🚀 快速开始

### 环境要求
- Ruby & Jekyll
- Node.js (部分脚本需要)
- Git

### 安装步骤
1.  克隆仓库：
    ```bash
    git clone https://github.com/HongyiYoung/HongyiYoung.github.io.git
    cd HongyiYoung.github.io
    ```
2.  安装依赖：
    ```bash
    bundle install
    ```
3.  本地运行：
    ```bash
    bundle exec jekyll serve
    ```

## 🛠️ 维护指南

### 1. 编辑主页内容 (`About`)
主页主要内容位于 **`_pages/about.md`** 文件中。
- **成绩/排名卡片 (Rank/GPA Cards)**：修改文件头部 (front matter) 里面底部的 HTML/CSS 类部分。我们在 `_sass/_custom.scss` 定义了样式，你只需要修改数值。
- **个人简介 (Biography)**：编辑 `content-en` (英文) 和 `content-zh` (中文) div 标签下的文本内容。
- **个人资料 (Profile Info)**：更新文件头部的 `profile` 部分信息。

### 2. 更新新闻 (News)
在 **`_news/`** 目录下添加新的 Markdown 文件。
- **命名规范**：文件名建议使用 `date-name.md` 格式，例如 `2026-01-01-scholarship.md`。
- **格式示例**：
  ```yaml
  ---
  layout: post
  date: 2026-01-01 07:59:00-0400
  inline: true
  related_posts: false
  ---

  这里写你的新闻内容，支持 **Markdown** 语法。
  ```

### 3. 更新简历 (CV / Resume)
简历数据由 **`assets/json/resume.json`** 文件驱动。
- **个人信息 (Basics)**：更新 `basics` 字段 (邮箱、电话、简介)。
- **工作经历 (Experience)**：在 `work` 数组中添加新条目。
- **教育经历 (Education)**：在 `education` 数组中添加新条目。
- **奖项 (Awards)**：在 `awards` 数组中添加新条目。

**注意**：JSON 值中请勿包含 HTML 标签。网站会自动格式化数据，并处理邮箱/电话的隐私保护弹窗。

### 4. 更新论文 (Publications)
论文列表由 `_bibliography/papers.bib` 驱动，我们在原版基础上进行了增强设计：
- **酷炫 Intro 弹窗**：在 `_includes/intros/` 目录下，新建与论文 bib key 同名的 Markdown 文件（例如 `yang2026vlm3d.md`，中文则为 `yang2026vlm3d_zh.md`）。在里面放入图文内容，页面上会自动生成一个 "Intro" 按钮，点击即可弹出深浅色自适应的酷炫模态框展示这些介绍！

### 5. 修改样式 (Styles)
- **自定义样式**：在 **`_sass/_custom.scss`** 中添加或修改样式。
- **全局配置**：通用设置（标题、描述、SEO等）在 **`_config.yml`** 中。

### 5. 多语言支持 (Internationalization)
本站采用目录分离的方式实现中英文切换：
- **自动化工具**:
  - 我们提供了一个 Python 脚本 **`scripts/auto_translate_setup.py`**，用于自动检查并创建缺失的中文新闻或项目文件。
  - **用法**: 运行 `python scripts/auto_translate_setup.py`。
  - **效果**: 它会扫描 `_news` 和 `_projects` 目录，如果发现 `english.md` 没有对应的 `english_zh.md`，会自动复制一份并在头部添加 `lang: zh`，你只需打开生成的文件进行翻译即可。

- **主页 (About)**:
  - 英文版：**`_pages/about.md`**
  - 中文版：**`ch/index.md`** (注意：**移动端样式修复**，如头像堆叠，已在 `_sass/_custom.scss` 中定义)。
- **简历 (CV)**:
  - 英文数据：**`assets/json/resume.json`**
  - 中文数据：**`assets/json/resume_zh.json`** (请复制英文版结构并翻译内容)
  - **界面文本 (Labels)**: 简历中的固定标签（如 "Education" vs "教育经历"）由 **`_data/ui_text.yml`** 管理。如果需要修改这些标题，请编辑该文件。
- **新闻 (News)**:
  - 英文新闻：无后缀或自定义，例如 `2025-01-01-news.md`
  - 中文新闻：建议文件名以 `_zh.md` 结尾，例如 `2025-01-01-news_zh.md`，并在 Front Matter 中设置 `lang: zh`。
- **项目 (Projects)**:
  - 中文项目：新建项目文件时，务必在头部添加 `lang: zh`，这样它们才会出现在中文版项目列表中。
- **论文 (Publications)**:
  - 中文介绍：对于带有 Intro 介绍的论文，请在 `_includes/intros/` 添加带 `_zh.md` 后缀的翻译文件（如 `key_zh.md`），系统会自动在中文模式下加载它。

### 7. 移动端适配 (Mobile Responsiveness)
针对手机端（特别是小屏设备如 iPhone 12/13/14 等）的特殊适配样式主要位于 **`_sass/_custom.scss`** 和 **`_includes/custom_styles.liquid`**。
- **Profile 布局**：在屏幕宽度 < 768px 时，强制头像与个人信息垂直堆叠 (`float: none`)。
- **Stat Cards**：在移动端强制显示为 2x2 网格，防止挤压。
- **Contact Badges**: 强制设置为 `inline-block` 以保证换行整齐。

## 📦 部署 (Deployment)
### 自动发布脚本 (推荐)
本仓库包含一个自动化发布脚本 **`release.sh`**，它可以一键完成“备份源码到 `source` 分支”和“发布网站到 `main` 分支”的操作。

**使用方法 (Windows 用户需在 Git Bash 或 WSL 中运行)**:
```bash
./release.sh "你的提交信息"
# 例如: ./release.sh "Update homepage content"
```

### 手动部署
如果你不使用脚本，也可以通过 Git 手动推送。通常建议将源码保存在 `source` 分支，而 `main` 分支仅用于存放 `_site` 生成的静态文件（如果使用 GitHub Pages 的话）。或者利用 GitHub Actions 自动构建（取决于你的 `.github/workflows` 配置）。

### 8. 国内访问优化 (China Accessibility)
由于 GitHub 统计图服务 (`vercel.app`) 在国内访问不稳，我们在 **`_config.yml`** 中提供了镜像配置：
```yaml
# 默认使用官方源 (需科学上网或 DNS 正常)
repo_stats_url: "https://github-readme-stats.vercel.app"

# 若国内无法访问，可尝试寻找自建镜像，例如:
# repo_stats_url: "https://github-readme-stats.lxzxl.cn"
```
如果图片加载失败，请检查此配置。修改 `_config.yml` 后需重启本地服务生效。
