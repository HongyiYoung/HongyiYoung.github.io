#!/bin/bash

# -----------------------------------------------------------------------------
# Jekyll 自动化部署脚本 (WSL/Linux 版)
# 功能：
# 1. 自动备份源码到 source 分支
# 2. 编译生成静态网站 (_site)
# 3. 将 _site 目录发布到 main 分支
# -----------------------------------------------------------------------------

# 配置
SOURCE_BRANCH="source"
DEPLOY_BRANCH="main"
BUILD_DIR="_site"
COMMIT_MSG="$1"

# 颜色输出
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
QC='\033[0m' # No Color

echo -e "${GREEN}=========================================${QC}"
echo -e "${GREEN}   Jekyll 自动化部署脚本 - 开始运行${QC}"
echo -e "${GREEN}=========================================${QC}"

# 0. 检查提交信息
if [ -z "$COMMIT_MSG" ]; then
  echo -e "${YELLOW}提示: 未提供提交信息，使用默认信息 'Update site content'${QC}"
  COMMIT_MSG="Update site content"
fi

# 1. 检查当前分支
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$CURRENT_BRANCH" != "$SOURCE_BRANCH" ]; then
    echo -e "${YELLOW}⚠️  警告：当前不在 $SOURCE_BRANCH 分支！(当前: $CURRENT_BRANCH)${QC}"
    read -p "是否继续？(y/n) " choice
    case "$choice" in 
      y|Y ) echo "继续执行...";;
      * ) echo "已取消"; exit 1;;
    esac
fi

# 2. 备份源码 (Source)
echo -e "\n${GREEN}[1/3] 正在备份源码到 $SOURCE_BRANCH 分支...${QC}"
git add .
git commit -m "$COMMIT_MSG"
git push origin "$SOURCE_BRANCH"

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ 源码推送失败，请检查 Git 状态。${QC}"
    exit 1
fi

# 3. 编译网站 (Build)
echo -e "\n${GREEN}[2/3] 正在编译 Jekyll 网站...${QC}"
# 确保使用 bundler 环境
mkdir -p _data
echo "last_updated: \"$(TZ=Asia/Shanghai date +'%Y-%m-%d')\"" > _data/build.yml
bundle exec jekyll build

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ 编译失败，请检查 Jekyll 日志。${QC}"
    exit 1
fi

# 4. 发布部署 (Deploy)
echo -e "\n${GREEN}[3/3] 正在发布到 $DEPLOY_BRANCH 分支...${QC}"

# 获取远程仓库地址
REMOTE_URL=$(git remote get-url origin)

# 进入构建目录
cd "$BUILD_DIR" || exit

# 初始化临时 Git 仓库
# 注意：这里我们每次都重新初始化，确保 main 分支只包含最新的构建产物
# 这样可以避免 _site 目录的历史包袱
git init
git checkout -b "$DEPLOY_BRANCH"
git add .
git commit -m "Deploy: $COMMIT_MSG"

# 添加远程仓库
git remote add origin "$REMOTE_URL"

# 强制推送到远程部署分支
# 注意：这会覆盖远程 main 分支的历史
git push -f origin "$DEPLOY_BRANCH":"$DEPLOY_BRANCH"

if [ $? -eq 0 ]; then
    echo -e "\n${GREEN}✅ 发布完成！${QC}"
    echo "源码已保存至: $SOURCE_BRANCH"
    echo "网站已更新至: $DEPLOY_BRANCH"
else
    echo -e "${RED}❌ 发布失败，请检查网络或权限。${QC}"
fi
