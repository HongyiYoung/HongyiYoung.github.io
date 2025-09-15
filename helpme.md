# 常用命令行
cd /mnt/c/AcademicPage
alias g='git add . && git commit -m "Update content"'
alias d='git push origin main'
alias rs='bundle exec jekyll serve'
alias s='docker compose up'
# 添加新闻
在`_news`处添加新md即可
# 添加项目
在`_projects`处添加新md即可，注意图片存放在形如“assets/img/autonomous_driving_2024/cover.png”的路径下
# 修改简历cv
修改文件在`assets\json\resume.json`而不是`cv.yml`