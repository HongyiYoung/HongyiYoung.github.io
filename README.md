# 个人主页项目维护指南

这份文档旨在帮助你（以及未来的维护者）快速上手这个基于 **Jekyll** 的个人主页项目。

## 📁 1. 项目结构说明

本项目使用了 `al-folio` 主题，主要文件结构如下：

*   **`_posts/`**: 博客文章存放处。格式为 `YYYY-MM-DD-title.md`。
*   **`_pages/`**: 独立页面（如 About, Publications 等）。
*   **`_bibliography/`**: 存放论文引用文件 (`papers.bib`)。
*   **`assets/`**: 图片、PDF、CSS 等静态资源。
    *   `assets/img/`: 图片
    *   `assets/pdf/`: 简历或论文 PDF
*   **`_config.yml`**: **核心配置文件**。修改网站标题、个人信息、菜单栏等都在这里。
*   **`Gemfile`**: 定义了项目所需的 Ruby 插件依赖。
*   **`release.sh`**: **自动化发布脚本**（Bash 脚本，适用于 WSL/Linux）。

---

## 🛠️ 2. 环境搭建 (从零开始)

如果你换了一台新电脑（Windows/WSL/macOS），通过以下步骤恢复开发环境：

### 第一步：安装基础软件
1.  **Git**: [下载地址](https://git-scm.com/)
2.  **Ruby**: Jekyll 是基于 Ruby 的。
    *   **Windows**: 推荐使用 [RubyInstaller](https://rubyinstaller.org/) (下载 With Devkit 版本)。
    *   **WSL/Linux**: `sudo apt-get install ruby-full build-essential zlib1g-dev`
3.  **Bundler**: 安装完 Ruby 后，在终端运行：
    ```bash
    gem install bundler
    ```

### 第二步：下载源码
```bash
# 克隆仓库（如果你还没有下载）
git clone <你的仓库地址>
cd <你的项目目录>

# 切换到源码分支 (非常重要！)
git checkout source
```

### 第三步：安装依赖
在项目根目录下运行：
```bash
bundle install
```
*如果遇到网络问题，可以尝试更换 RubyGems 国内镜像源。*

---

## 🚀 3. 常用命令

### 本地预览 (最常用)
在浏览器中实时预览修改效果：
```bash
bundle exec jekyll serve
```
*   访问地址通常是: `http://localhost:4000`
*   按 `Ctrl + C` 停止运行。

### 手动编译
如果不启动服务器，只生成静态文件到 `_site` 目录：
```bash
bundle exec jekyll build
```

---

## 📦 4. 一键发布 (如何使用 release.sh)

我们制定了以下分支策略：
*   **`source` 分支**: 存放所有源代码（你写文章、改配置的地方）。
*   **`main` (或 master) 分支**: 存放编译后的网页代码（GitHub Pages 展示的内容）。

### 发布步骤
当你完成修改并准备发布时，**不需要**手动分别推送两个分支。只需运行根目录下的 `release.sh` 脚本。

#### WSL / Linux / macOS
在终端中运行：
```bash
# 第一次运行前，需要给脚本添加执行权限
chmod +x release.sh

# 执行发布
./release.sh "这里写你的更新说明"
```
*如果不写说明，默认会使用 "Update site content"*

**脚本会自动完成以下工作：**
1.  将当前源码 `git commit` 并推送到 `source` 分支。
2.  执行 `jekyll build` 编译生成网站。
3.  将生成的 `_site` 文件夹内容强制推送到 `main` 分支。

---

## ❓ 常见问题

**Q: 为什么我看不到我修改的内容？**
A: 请确保你正在编辑的分支是 `source`。发布后，GitHub Pages 可能需要 1-2 分钟更新，请耐心等待或强制刷新浏览器 (Ctrl+F5)。

**Q: 脚本提示 `Permission denied`？**
A: 请运行 `chmod +x release.sh` 赋予脚本执行权限。

**Q: 为什么 `_site` 目录在 `.gitignore` 里？**
A: 因为 `_site` 是生成产物，不需要保存在 `source` 分支中。我们的脚本会专门处理它的发布的可追溯性。
