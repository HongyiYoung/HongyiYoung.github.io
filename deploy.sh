#!/bin/sh
# 这是一个自动部署脚本

# 检查是否提供了提交信息
if [ -z "$1" ]; then
  echo "❌ 错误：请提供一个提交信息！"
  echo "用法: ./deploy.sh \"你的更新说明\""
  exit 1
fi

# 执行 Git 命令
echo "🚀 1/3: 添加所有文件..."
git add .

echo "📝 2/3: 提交更改..."
git commit -m "$1"

echo "📤 3/3: 推送到 GitHub..."
git push origin source

echo "✅ 部署完成！"
