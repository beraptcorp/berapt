#!/usr/bin/env python3
"""
Build static HTML pages for the Insights blog section.

Usage:
    pip install PyYAML markdown
    python scripts/build_insights.py

What it does:
    - Scans posts/*.md (skips files starting with _)
    - Generates insights/index.html (post list)
    - Generates insights/[slug]/index.html (individual posts)
"""

import os
import re
import shutil
from datetime import datetime, date
from pathlib import Path

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML 설치 필요: pip install PyYAML")

try:
    import markdown
except ImportError:
    raise SystemExit("markdown 설치 필요: pip install markdown")

# ─── Configuration ────────────────────────────────────────────────────────────

ROOT = Path(__file__).parent.parent
POSTS_DIR = ROOT / "posts"
INSIGHTS_DIR = ROOT / "insights"
BASE_URL = "https://www.berapt.com"
SITE_NAME = "비랩트"
DEFAULT_OG_IMAGE = f"{BASE_URL}/images/beraptBlackLogo.png"

# TODO: Replace with your Google AdSense publisher ID (e.g., ca-pub-1234567890123456)
ADSENSE_PUBLISHER_ID = "ca-pub-XXXXXXXXXXXXXXXXX"
# TODO: Replace with your AdSense ad unit IDs after creating them in AdSense dashboard
ADSENSE_SLOT_TOP = "XXXXXXXXXX"
ADSENSE_SLOT_BOTTOM = "XXXXXXXXXX"
ADSENSE_SLOT_LIST = "XXXXXXXXXX"

# ─── Helpers ──────────────────────────────────────────────────────────────────

def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and return (metadata, body)."""
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end != -1:
            fm_text = content[3:end].strip()
            body = content[end + 4:].strip()
            try:
                return yaml.safe_load(fm_text) or {}, body
            except yaml.YAMLError:
                pass
    return {}, content


def slugify(filename: str) -> str:
    """Convert filename to URL slug."""
    return Path(filename).stem


def format_date(d) -> str:
    """Format date for display."""
    if isinstance(d, (date, datetime)):
        return d.strftime("%Y년 %m월 %d일")
    try:
        return datetime.strptime(str(d), "%Y-%m-%d").strftime("%Y년 %m월 %d일")
    except (ValueError, TypeError):
        return str(d) if d else ""


def iso_date(d) -> str:
    """Format date as ISO string."""
    if isinstance(d, (date, datetime)):
        return d.isoformat()
    return str(d) if d else ""


def render_markdown(text: str) -> str:
    """Render markdown to HTML. All links open in a new tab."""
    md = markdown.Markdown(
        extensions=["fenced_code", "tables", "attr_list"],
        extension_configs={},
    )
    html = md.convert(text)
    html = re.sub(r'<a ', '<a target="_blank" rel="noopener noreferrer" ', html)
    # 출처/참고 헤딩 바로 뒤 ul에 post-sources 클래스 부여
    html = re.sub(
        r'(<h[23][^>]*>(?:출처|참고\s*자료|참고|References?|Sources?)</h[23]>\s*)<ul>',
        r'\1<ul class="post-sources">',
        html,
        flags=re.IGNORECASE,
    )
    return html


def truncate(text: str, length: int = 120) -> str:
    """Remove HTML tags and truncate for descriptions."""
    clean = re.sub(r"<[^>]+>", "", text)
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean[:length] + "…" if len(clean) > length else clean

# ─── HTML Fragments ───────────────────────────────────────────────────────────

def head_html(title: str, description: str, url: str, image: str, is_article: bool = False, pub_date: str = "") -> str:
    og_type = "article" if is_article else "website"
    article_meta = f'    <meta property="article:published_time" content="{pub_date}">\n' if is_article and pub_date else ""
    return f"""    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="apple-touch-icon" sizes="180x180" href="https://www.berapt.com/favicons/apple-icon-180x180.png">
    <link rel="icon" type="image/png" sizes="32x32" href="https://www.berapt.com/favicons/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="https://www.berapt.com/favicons/favicon-16x16.png">
    <link rel="icon" type="image/x-icon" href="https://www.berapt.com/favicons/favicon.ico">
    <link rel="manifest" href="https://www.berapt.com/favicons/manifest.json">
    <meta name="author" content="{SITE_NAME}">
    <meta name="robots" content="index, follow">
    <title>{title} - {SITE_NAME}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{url}">
    <meta property="og:site_name" content="{SITE_NAME}">
    <meta property="og:locale" content="ko_KR">
    <meta property="og:type" content="{og_type}">
    <meta property="og:title" content="{title} - {SITE_NAME}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{image}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
{article_meta}    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title} - {SITE_NAME}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{image}">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/styles/main.css">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_PUBLISHER_ID}" crossorigin="anonymous"></script>"""


def nav_html(active: str = "insights") -> str:
    links = [
        ("#vision", "비전", "vision"),
        ("#services", "서비스", "services"),
        ("#occ", "OCC", "occ"),
        ("#activities", "활동", "activities"),
        ("#history", "업력", "history"),
        ("#news", "뉴스", "news"),
        ("#contact", "Contact", "contact"),
    ]
    desktop_items = "\n".join(
        f'                <li><a href="/{href}" class="nav-link{" active" if section == active else ""}" data-section="{section}">{label}</a></li>'
        for href, label, section in links
    )
    desktop_items += f'\n                <li><a href="/insights/" class="nav-link{" active" if active == "insights" else ""}" data-section="insights">인사이트</a></li>'

    mobile_items = "\n".join(
        f'            <li><a href="/{href}" class="mobile-nav-link">{ label}</a></li>'
        for href, label, _ in links
    )
    mobile_items += '\n            <li><a href="/insights/" class="mobile-nav-link">인사이트</a></li>'

    return f"""    <nav class="sticky-nav" id="sticky-nav">
        <div class="nav-inner">
            <a href="/" class="nav-logo">
                <img src="/images/beraptBlackLogo.png" alt="비랩트" />
            </a>
            <ul class="nav-links">
{desktop_items}
            </ul>
            <button class="nav-hamburger" id="nav-hamburger" aria-label="메뉴">
                <span></span><span></span><span></span>
            </button>
        </div>
    </nav>

    <div class="mobile-menu" id="mobile-menu">
        <ul>
{mobile_items}
        </ul>
    </div>"""


def footer_html() -> str:
    return """    <footer class="site-footer">
        <div class="footer-inner">
            <b>주식회사 비랩트</b>
            <span>사업자 등록번호 : 411-88-02619 · 통신판매업 신고번호 : 제2022-서울강남-05265호</span>
            <span>대표 : 이원제 · 전화 : 070-4115-4732 · 주소 : 서울시 강서구 마곡중앙8로 14 406호 (07801)</span>
        </div>
    </footer>"""


def nav_script() -> str:
    return """    <script>
        document.getElementById('nav-hamburger').addEventListener('click', function() {
            this.classList.toggle('open');
            document.getElementById('mobile-menu').classList.toggle('open');
        });
        document.querySelectorAll('.mobile-nav-link').forEach(link => {
            link.addEventListener('click', () => {
                document.getElementById('mobile-menu').classList.remove('open');
                document.getElementById('nav-hamburger').classList.remove('open');
            });
        });
    </script>"""


def ad_unit(slot_id: str, label: str = "") -> str:
    comment = f"<!-- Ad: {label} -->\n    " if label else ""
    return f"""    {comment}<div class="ad-container">
        <ins class="adsbygoogle"
             style="display:block"
             data-ad-client="{ADSENSE_PUBLISHER_ID}"
             data-ad-slot="{slot_id}"
             data-ad-format="auto"
             data-full-width-responsive="true"></ins>
        <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
    </div>"""


def structured_data_article(meta: dict, slug: str, content_html: str) -> str:
    import json as _json
    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": meta.get("title", ""),
        "description": meta.get("description", ""),
        "datePublished": iso_date(meta.get("date", "")),
        "author": {"@type": "Organization", "name": meta.get("author", SITE_NAME)},
        "publisher": {
            "@type": "Organization",
            "name": SITE_NAME,
            "logo": {"@type": "ImageObject", "url": f"{BASE_URL}/images/beraptBlackLogo.png"},
        },
        "url": f"{BASE_URL}/insights/{slug}/",
        "image": meta.get("image", DEFAULT_OG_IMAGE) if meta.get("image", "").startswith("http") else f"{BASE_URL}{meta.get('image', '')}",
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{BASE_URL}/insights/{slug}/"},
    }
    return _json.dumps(data, ensure_ascii=False, indent=2)

# ─── Page Generators ──────────────────────────────────────────────────────────

def post_nav_html(prev_post, next_post) -> str:
    """이전글/다음글 + 목록 버튼 영역."""

    def nav_card(p: dict, direction: str) -> str:
        label = "← 이전글" if direction == "prev" else "다음글 →"
        align = "post-nav-card--prev" if direction == "prev" else "post-nav-card--next"
        img = p["meta"].get("image", "")
        thumb = f'<img src="{img}" alt="{p["meta"].get("title", "")}" class="nav-card-thumb">' if img else ""
        return f"""            <a href="/insights/{p['slug']}/" class="post-nav-card {align}">
                <span class="nav-card-label">{label}</span>
                <div class="nav-card-inner">
                    {thumb}
                    <div class="nav-card-text">
                        <time class="nav-card-date">{format_date(p["meta"].get("date", ""))}</time>
                        <strong class="nav-card-title">{p["meta"].get("title", p["slug"])}</strong>
                    </div>
                </div>
            </a>"""

    prev_html = nav_card(prev_post, "prev") if prev_post else '<div class="post-nav-card post-nav-card--empty"></div>'
    next_html = nav_card(next_post, "next") if next_post else '<div class="post-nav-card post-nav-card--empty"></div>'

    return f"""    <div class="post-nav-section">
        <div class="insights-inner">
            <a href="/insights/" class="post-nav-list-btn">인사이트 목록으로</a>
            <div class="post-nav-grid">
{prev_html}
{next_html}
            </div>
        </div>
    </div>"""


def build_post_page(slug: str, meta: dict, body_html: str, prev_post=None, next_post=None) -> str:
    title = meta.get("title", slug)
    description = meta.get("description", truncate(body_html))
    raw_image = meta.get("image", "")
    image = f"{BASE_URL}{raw_image}" if raw_image and not raw_image.startswith("http") else (raw_image or DEFAULT_OG_IMAGE)
    post_url = f"{BASE_URL}/insights/{slug}/"
    pub_date = iso_date(meta.get("date", ""))
    display_date = format_date(meta.get("date", ""))
    author = meta.get("author", SITE_NAME)
    tags = meta.get("tags", []) or []
    tags_html = "".join(f'<span class="post-tag">{t}</span>' for t in tags)
    sd = structured_data_article(meta, slug, body_html)

    if raw_image:
        hero_html = f"""    <div class="post-hero post-hero--image">
        <img src="{raw_image}" alt="{title}" class="post-hero-img">
        <div class="post-hero-overlay">
            <div class="insights-inner">
                <a href="/insights/" class="insights-back">← 인사이트 목록</a>
                <h1 class="post-title">{title}</h1>
                <div class="post-meta-row">
                    <time datetime="{pub_date}" class="post-date">{display_date}</time>
                    {f'<span class="post-author">by {author}</span>' if author else ""}
                    <div class="post-tags">{tags_html}</div>
                </div>
            </div>
        </div>
    </div>"""
    else:
        hero_html = f"""    <div class="post-hero post-hero--no-image">
        <div class="insights-inner">
            <a href="/insights/" class="insights-back">← 인사이트 목록</a>
            <h1 class="post-title">{title}</h1>
            <div class="post-meta-row">
                <time datetime="{pub_date}" class="post-date">{display_date}</time>
                {f'<span class="post-author">by {author}</span>' if author else ""}
                <div class="post-tags">{tags_html}</div>
            </div>
        </div>
    </div>"""

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
{head_html(title, description, post_url, image, is_article=True, pub_date=pub_date)}
    <script type="application/ld+json">
{sd}
    </script>
</head>
<body>

{nav_html("insights")}

{hero_html}

{ad_unit(ADSENSE_SLOT_TOP, "article-top")}

    <article class="post-body">
        <div class="insights-inner">
{body_html}
        </div>
    </article>

{ad_unit(ADSENSE_SLOT_BOTTOM, "article-bottom")}

{post_nav_html(prev_post, next_post)}

{footer_html()}

{nav_script()}
</body>
</html>"""


def inject_insights_preview(posts: list) -> None:
    """홈페이지 index.html의 플레이스홀더에 최신 글 미리보기를 삽입."""
    index_path = ROOT / "index.html"
    content = index_path.read_text(encoding="utf-8")

    if not posts:
        snippet = ""
    else:
        cards = ""
        for p in posts:
            meta = p["meta"]
            img = meta.get("image", "")
            thumb = f'<div class="hp-insight-thumb"><img src="{img}" alt="{meta.get("title", "")}"></div>' if img else '<div class="hp-insight-thumb hp-insight-thumb--empty"></div>'
            tags = meta.get("tags", []) or []
            tags_html = "".join(f'<span class="post-tag">{t}</span>' for t in tags[:2])
            cards += f"""                <a href="/insights/{p['slug']}/" class="hp-insight-card">
                    {thumb}
                    <div class="hp-insight-card-body">
                        <time class="post-date">{format_date(meta.get("date", ""))}</time>
                        <strong class="hp-insight-card-title">{meta.get("title", p["slug"])}</strong>
                        <p class="hp-insight-card-desc">{meta.get("description", "")}</p>
                        <div class="post-tags">{tags_html}</div>
                    </div>
                </a>
"""
        snippet = f"""    <section class="section-insights-preview">
        <div class="section-inner">
            <p class="section-label">Insights</p>
            <h2 class="section-headline">인사이트</h2>
            <div class="hp-insights-grid">
{cards}            </div>
            <div class="hp-insights-more">
                <a href="/insights/" class="hp-insights-more-btn">모든 글 보기 →</a>
            </div>
        </div>
    </section>"""

    new_content = re.sub(
        r"<!-- INSIGHTS_PREVIEW_START -->.*?<!-- INSIGHTS_PREVIEW_END -->",
        f"<!-- INSIGHTS_PREVIEW_START -->\n{snippet}\n    <!-- INSIGHTS_PREVIEW_END -->",
        content,
        flags=re.DOTALL,
    )
    index_path.write_text(new_content, encoding="utf-8")


def build_index_page(posts: list[dict]) -> str:
    title = "인사이트"
    description = f"{SITE_NAME}의 서브컬처 창작 생태계, 플랫폼 이야기, 창작자 인사이트를 공유합니다."
    url = f"{BASE_URL}/insights/"
    image = DEFAULT_OG_IMAGE

    cards_html = ""
    for p in posts:
        slug = p["slug"]
        meta = p["meta"]
        card_image = meta.get("image", "")
        card_img_html = f'<div class="card-image"><img src="{card_image}" alt="{meta.get("title", "")}"></div>' if card_image else '<div class="card-image card-image--placeholder"></div>'
        tags = meta.get("tags", []) or []
        tags_html = "".join(f'<span class="post-tag">{t}</span>' for t in tags[:3])
        cards_html += f"""        <a href="/insights/{slug}/" class="insights-card">
{card_img_html}
            <div class="card-body">
                <time class="post-date">{format_date(meta.get("date", ""))}</time>
                <h2 class="card-title">{meta.get("title", slug)}</h2>
                <p class="card-desc">{meta.get("description", "")}</p>
                <div class="post-tags">{tags_html}</div>
                <span class="card-read-more">자세히 보기 →</span>
            </div>
        </a>
"""

    empty_html = ""
    if not posts:
        empty_html = '<p class="insights-empty">아직 게시된 글이 없습니다.</p>'

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
{head_html(title, description, url, image)}
</head>
<body>

{nav_html("insights")}

    <div class="insights-hero">
        <div class="insights-inner">
            <p class="section-label">Insights</p>
            <h1 class="insights-hero-title">인사이트</h1>
            <p class="insights-hero-sub">서브컬처 창작 생태계, 플랫폼 이야기, 창작자 인사이트를 공유합니다.</p>
        </div>
    </div>

{ad_unit(ADSENSE_SLOT_LIST, "list-top")}

    <section class="insights-list-section">
        <div class="insights-inner">
            <div class="insights-grid">
{cards_html}            </div>
{empty_html}
        </div>
    </section>

{footer_html()}

{nav_script()}
</body>
</html>"""

# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    INSIGHTS_DIR.mkdir(exist_ok=True)

    posts = []
    for md_file in sorted(POSTS_DIR.glob("*.md")):
        if md_file.name.startswith("_"):
            print(f"  skip (draft): {md_file.name}")
            continue

        raw = md_file.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)
        body_html = render_markdown(body)
        slug = slugify(md_file.name)

        posts.append({"slug": slug, "meta": meta, "body_html": body_html})
        print(f"  found: {md_file.name} → /insights/{slug}/")

    # Sort by date descending
    def sort_key(p):
        d = p["meta"].get("date", "")
        if isinstance(d, (date, datetime)):
            return d.isoformat()
        return str(d)

    posts.sort(key=sort_key, reverse=True)

    # Generate individual post pages
    for i, p in enumerate(posts):
        # 날짜 내림차순이므로: next(더 최신) = i-1, prev(더 오래된) = i+1
        next_post = posts[i - 1] if i > 0 else None
        prev_post = posts[i + 1] if i + 1 < len(posts) else None
        slug = p["slug"]
        post_dir = INSIGHTS_DIR / slug
        post_dir.mkdir(exist_ok=True)
        html = build_post_page(slug, p["meta"], p["body_html"], prev_post, next_post)
        (post_dir / "index.html").write_text(html, encoding="utf-8")
        print(f"  built: insights/{slug}/index.html")

    # Generate index page
    index_html = build_index_page(posts)
    (INSIGHTS_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print(f"  built: insights/index.html ({len(posts)} posts)")

    # Inject insights preview into homepage
    inject_insights_preview(posts[:4])
    print(f"  updated: index.html (insights preview, {min(4, len(posts))} posts)")

    print(f"\n완료! {len(posts)}개 게시글 빌드됨.")


if __name__ == "__main__":
    main()
