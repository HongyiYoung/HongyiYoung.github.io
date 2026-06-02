import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def require(condition, message):
    if not condition:
        raise AssertionError(message)


layout = read("_layouts/about.liquid")
header = read("_includes/header.liquid")
custom = read("_sass/_custom.scss")
inline_custom = read("_includes/custom_styles.liquid")
base_styles = read("_sass/_base.scss")
cv_styles = read("_sass/_cv.scss")
theme_styles = read("_sass/_themes.scss")
cache_bust_plugin = read("_plugins/cache-bust.rb")
social_include = read("_includes/social.liquid")
news_include = read("_includes/news.liquid")
resume_skills_include = read("_includes/resume/skills.liquid")
resume_interests_include = read("_includes/resume/interests.liquid")
resume_languages_include = read("_includes/resume/languages.liquid")
about = read("_pages/about.md")
zh_about = read("ch/index.md")
resume_en = read("assets/json/resume.json")
resume_zh = read("assets/json/resume_zh.json")
legacy_cv = read("_data/cv.yml")
resume_tex = read("resume_content.tex")
electronic_project = read("_projects/electronic_design_2025.md")
electronic_project_zh = read("_projects/electronic_design_2025_zh.md")
admin_data = read("admin_data.js")
resume_en_data = json.loads(resume_en)
resume_zh_data = json.loads(resume_zh)
language_toggle_block = base_styles.split("\n\n.language-toggle {\n", 1)[1].split("\n}", 1)[0]

require("profile_onerror" not in layout, "profile image should not have timestamp retry onerror")
require("cache_bust=true" not in layout, "profile image should not force cache-busted URLs")
require('loading="eager"' in layout, "profile image should keep eager loading")
require("fetchpriority=\"high\"" in layout, "profile image should request high fetch priority")
require("profile_image_fast_path" in layout, "profile image should use an optimized profile image path")
require("-480.webp" in layout, "profile image should use the generated 480w WebP asset")

require("ZhiMangXingNameSubset" in custom, "custom stylesheet should define the expressive name font subset")
require("ZhiMangXing-name-subset.woff2" in custom, "custom stylesheet should load the expressive WOFF2 subset")
require("font-display: swap" in custom, "name font should not block text rendering")
require("name-calligraphy" in layout, "layout should use the subset-backed name style")
require("font-family: 'ZhiMangXingNameSubset'" in custom, "name style should use the expressive subset font family")
require("language-toggle" in header, "header should expose an explicit language toggle")
require("Change language" in header, "language toggle should have an English title")
require("切换语言" in header, "language toggle should expose a Chinese label")
require(
    'class="toggle-container search-toggle-container"' in header,
    "search toggle should use the same flex container as theme/language toggles",
)
require(
    "#light-toggle,\n#search-toggle,\n.language-toggle" in base_styles,
    "language toggle should share the same nav action sizing as search/theme buttons",
)
require(
    ".search-toggle-container" in base_styles,
    "search toggle container should be explicitly centered with the other nav actions",
)
require(
    "#search-toggle .nav-link {\n  color: inherit;" in base_styles
    and "#search-toggle i {\n  color: inherit;" in base_styles,
    "search toggle internals should inherit theme-aware button color",
)
require(
    ".language-toggle {\n  font-size" in base_styles and "border:" not in language_toggle_block,
    "language toggle should not render with an outer border",
)
require(
    "border-radius:" not in language_toggle_block,
    "language toggle should not render as a pill/circle",
)
require(
    "@media (max-width: 575.98px)" in base_styles
    and "#navbarNav .navbar-nav" in base_styles
    and ".toggle-container" in base_styles,
    "mobile navbar should explicitly center collapsed nav actions",
)
require(
    "#light-toggle-system,\n#light-toggle-dark,\n#light-toggle-light" in theme_styles
    and "padding-left: 10px" not in theme_styles
    and "padding-top: 12px" not in theme_styles,
    "theme icons should be centered by the button layout, not hard-coded padding",
)
require(
    ".contact-icons" in base_styles
    and ".cv-icon-svg" in base_styles
    and "<style>" not in social_include,
    "CV icon sizing should live in shared SCSS instead of inline include styles",
)
require(
    "@media (max-width: 575.98px)" in base_styles
    and ".contact-icons" in base_styles
    and ".cv-icon-svg" in base_styles,
    "mobile contact icons should keep CV and email visually matched",
)
require(
    "background: rgba(var(--global-theme-color-rgb)" not in base_styles
    and "border-radius: 50%" not in base_styles
    and "font-size: 1.3em" not in base_styles,
    "legacy mobile contact icon styling should not override the shared CV/email sizing",
)
require(
    "transform: translateY(0.08em)" in custom and "vertical-align: baseline" in custom,
    "name calligraphy should be baseline-adjusted for the current font",
)
for styles in (custom, inline_custom):
    require("linear-gradient(135deg" not in styles, "stat cards should avoid bright fixed gradients")
    require("var(--stat-card-bg)" in styles, "stat cards should use theme-aware custom properties")
    require("html[data-theme=\"dark\"]" in styles, "stat cards should define a dark-theme palette")

for text in (about, zh_about):
    require("Merit Student" in text or "三好学生" in text, "homepage should mention merit student")
    require(
        "Outstanding Student Cadre" in text or "优秀学生干部" in text,
        "homepage should mention outstanding student cadre",
    )

def has_award(data, title, date):
    return any(award.get("title") == title and award.get("date") == date for award in data.get("awards", []))


require(
    has_award(resume_en_data, "Merit Student of Southwest University", "2024-10"),
    "English resume should show 2024-10 merit student award without a day",
)
require(
    has_award(resume_en_data, "Outstanding Student Cadre of Southwest University", "2024-10"),
    "English resume should show 2024-10 cadre award without a day",
)
require(
    has_award(resume_zh_data, "西南大学三好学生", "2024-10"),
    "Chinese resume should show 2024-10 merit student award without a day",
)
require(
    has_award(resume_zh_data, "西南大学优秀学生干部", "2024-10"),
    "Chinese resume should show 2024-10 cadre award without a day",
)

for data in (resume_en_data, resume_zh_data):
    patent_awards = [
        award
        for award in data.get("awards", [])
        if award.get("title") in {"National Invention Patent", "国家发明专利"}
    ]
    require(patent_awards, "resume should include the invention patent award")
    require(
        all(award.get("url") == "https://cponline.cnipa.gov.cn/" for award in patent_awards),
        "invention patent should link to CNIPA online portal",
    )

require("省级" not in resume_zh, "Chinese resume should use 省部级 instead of 省级")
require("省部级" in resume_zh, "Chinese resume should mention 省部级 awards")

require(
    "experience in Multimodal Large Models, Computer Vision, and Embedded Development" in resume_en_data["basics"]["summary"],
    "English resume about summary should mention multimodal, computer vision, and embedded development experience",
)
require(
    "有多模态大模型、计算机视觉、嵌入式等开发经验" in resume_zh_data["basics"]["summary"],
    "Chinese resume about summary should mention multimodal, computer vision, and embedded development experience",
)
require(
    "experience in Multimodal Large Models, Computer Vision, and Embedded Development" in about,
    "English homepage about should mention multimodal, computer vision, and embedded development experience",
)
require(
    "有多模态大模型、计算机视觉、嵌入式等开发经验" in zh_about,
    "Chinese homepage about should mention multimodal, computer vision, and embedded development experience",
)

require(
    [skill["name"] for skill in resume_en_data["skills"]] == ["Programming Languages", "Artificial Intelligence"],
    "English resume skills should keep only programming languages and artificial intelligence",
)
require(
    [skill["name"] for skill in resume_zh_data["skills"]] == ["编程语言", "人工智能"],
    "Chinese resume skills should keep only programming languages and artificial intelligence",
)
require(
    resume_en_data["skills"][1]["keywords"] == [
        "MLLM",
        "DL",
        "CV",
        "NLP",
    ],
    "English AI skills should use compact MLLM/DL/CV/NLP labels",
)
require(
    resume_zh_data["skills"][1]["keywords"] == ["MLLM", "DL", "CV", "NLP"],
    "Chinese AI skills should use compact MLLM/DL/CV/NLP labels",
)
require("resume-skill-groups" in resume_skills_include, "skills include should expose a CV-specific style hook")
require(
    "resume-keyword-with-level" in resume_skills_include
    and "resume-keyword-name" in resume_skills_include
    and "resume-keyword-level" in resume_skills_include,
    "skills include should split programming-language names and proficiency levels onto separate lines",
)
require("resume-interest-groups" in resume_interests_include, "interests include should expose a CV-specific style hook")
require(".resume-skill-groups" in cv_styles, "CV stylesheet should style the compact skills section")
require("grid-template-columns: repeat(2, minmax(0, 1fr))" in cv_styles, "CV skills should render keywords as an equal 2x2 grid")
require(
    ".resume-keyword-with-level" in cv_styles
    and ".resume-keyword-level" in cv_styles,
    "CV stylesheet should style split programming-language proficiency labels",
)
require(
    "Visited 20+ provinces in China" in resume_en
    and "Visited 20+ provinces and regions in China" not in resume_en
    and "Visited 20+ provinces and regions in China" not in legacy_cv,
    "English travel interest should say Visited 20+ provinces in China",
)
require(
    "游历中国20+省份" in resume_zh and "省份及地区" not in resume_zh,
    "Chinese travel interest should sync the 20+ provinces wording",
)
require(".resume-interest-groups" in cv_styles, "CV stylesheet should style the compact interests section")
require(
    "resume-interest-card" in resume_interests_include,
    "interests include should expose dedicated card hooks for cleaner layout",
)
require(
    "div.resume-interest-groups {\n  display: grid;" in cv_styles
    and "grid-template-columns: repeat(3, minmax(0, 1fr))" in cv_styles,
    "CV interests should use a stable equal three-column grid on desktop",
)
require(
    ".resume-interest-groups .resume-keyword-list" in cv_styles
    and "grid-template-columns: 1fr" in cv_styles,
    "CV interest keywords should use uniform full-width rows",
)
require(
    "resume-language-groups" in resume_languages_include
    and "resume-language-card" in resume_languages_include,
    "languages include should expose dedicated hooks for compact layout",
)
require(
    "div.resume-language-groups {\n  display: grid;" in cv_styles
    and "grid-template-columns: repeat(3, minmax(0, 1fr))" in cv_styles,
    "CV languages should use a compact equal three-column grid",
)
require("max-width: 34rem" in cv_styles, "CV languages should not stretch across the full section width")
require(
    "directory: '_sass'" in cache_bust_plugin,
    "CSS cache busting should hash the real _sass directory instead of an empty path",
)

featured_news = [
    "2025Scholarship",
    "2025honors",
    "Electronic",
    "finalist",
    "2024Scholarship",
]
for slug in featured_news:
    require(f"featured: true" in read(f"_news/{slug}.md"), f"English featured news missing: {slug}")
    require(f"featured: true" in read(f"_news/{slug}_zh.md"), f"Chinese featured news missing: {slug}")

for slug in ["patent", "lanqiao", "cumcm", "2024honors"]:
    require(f"featured: true" not in read(f"_news/{slug}.md"), f"English non-homepage news should not be featured: {slug}")
    require(f"featured: true" not in read(f"_news/{slug}_zh.md"), f"Chinese non-homepage news should not be featured: {slug}")

require(
    "where: 'featured', true" in news_include and "news_featured" in news_include,
    "homepage news include should prefer featured items when limited",
)
require("省级一等奖" not in read("_news/Electronic_zh.md"), "Chinese electronic news should use 省部级一等奖")
require("省部级一等奖" in read("_news/Electronic_zh.md"), "Chinese electronic news should mention 省部级一等奖")
require("Provincial Level" in read("_news/Electronic.md"), "English electronic news should use Provincial Level")
for path, text in {
    "ch/index.md": zh_about,
    "assets/json/resume_zh.json": resume_zh,
    "resume_content.tex": resume_tex,
    "_projects/electronic_design_2025_zh.md": electronic_project_zh,
    "admin_data.js": admin_data,
}.items():
    require("省级一等奖" not in text, f"{path} should use 省部级一等奖 instead of 省级一等奖")
    require("省级二等奖" not in text, f"{path} should use 省部级二等奖 instead of 省级二等奖")
for path, text in {
    "_pages/about.md": about,
    "assets/json/resume.json": resume_en,
    "_data/cv.yml": legacy_cv,
    "_projects/electronic_design_2025.md": electronic_project,
    "_news/Electronic.md": read("_news/Electronic.md"),
    "_news/cumcm.md": read("_news/cumcm.md"),
    "admin_data.js": admin_data,
}.items():
    require("Provincial/Ministerial" not in text, f"{path} should use Provincial in English")
require("Provincial 1st Prize" in about, "English homepage awards should use Provincial 1st Prize")
require("Provincial First Prize" in electronic_project, "English project page should use Provincial First Prize")
require("省部级一等奖" in electronic_project_zh, "Chinese project page should use 省部级一等奖")
require("省部级一等奖" in resume_tex and "省部级二等奖" in resume_tex, "TeX resume should use 省部级 wording")
require("profile-info-card" in about and "profile-info-card" in zh_about, "profile info should use the compact card markup")
require(".profile-info-card" in custom and ".profile-info-item" in custom, "profile info card styles should be defined")
require(
    ".profile-info-card" in inline_custom and ".profile-info-item" in inline_custom,
    "inlined custom styles should style the profile info card loaded by the page",
)

for asset in ("assets/img/prof_pic.jpg", "assets/fonts/ZhiMangXing-name-subset.woff2"):
    require((ROOT / asset).exists(), f"missing optimized asset: {asset}")

if (ROOT / "_site").exists():
    require(
        (ROOT / "_site/assets/img/prof_pic-480.webp").exists(),
        "built site should contain the generated profile WebP asset",
    )

print("Homepage asset checks passed.")
