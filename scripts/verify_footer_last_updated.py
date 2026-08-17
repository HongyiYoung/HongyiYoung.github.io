from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


footer = read("_includes/footer.liquid")
site_config = read("_config.yml")

assert "Last updated: {{ site.time | date: '%B %d, %Y' }}." in footer, (
    "footer should use the current Jekyll build time for Last updated"
)
assert "site.data.build.last_updated" not in footer, (
    "footer should not depend on ignored _data/build.yml, which can go stale"
)
assert "timezone: Asia/Shanghai" in site_config, (
    "Jekyll should format build dates in the site's expected timezone"
)

print("Footer last-updated checks passed.")
