
# blogger_to_github.py
# Converts Blogger export XML (Settings > Manage Blog > Back up content) to GitHub Pages posts
import xml.etree.ElementTree as ET, json, re, os, html, datetime

BLOGGER_XML = "blog-01-01-2024.xml"  # <-- put your export file here
OUTPUT_DIR = "posts"
JSON_FILE = "posts.json"

ns = {"atom":"http://www.w3.org/2005/Atom"}
posts = []

tree = ET.parse(BLOGGER_XML)
root = tree.getroot()

for entry in root.findall("atom:entry", ns):
    # skip pages/comments
    cats = [c.get("term") for c in entry.findall("atom:category", ns)]
    if "http://schemas.google.com/blogger/2008/kind#post" not in str(entry):
        # check kind
        kind = entry.find("atom:category[@scheme='http://schemas.google.com/g/2005#kind']", ns)
        if kind is not None and "post" not in kind.get("term",""):
            continue

    title_el = entry.find("atom:title", ns)
    title = title_el.text if title_el is not None else "Untitled"
    content_el = entry.find("atom:content", ns)
    content = content_el.text if content_el is not None else ""
    published_el = entry.find("atom:published", ns)
    date = published_el.text[:10] if published_el is not None else "2024-01-01"

    # create slug
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')[:60]
    filename = f"{slug}.html"

    # snippet = first 200 chars stripped
    snippet = re.sub('<[^<]+?>', '', content)[:200] + "..."

    # write post html using template (you can copy template from sample)
    posts.append({
        "id": slug,
        "title": title,
        "url": f"posts/{filename}",
        "date": date,
        "snippet": snippet,
        "thumbnail": "",
        "body": content  # keep full HTML
    })

# sort by date desc
posts = sorted(posts, key=lambda x: x['date'], reverse=True)

# save json
with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(posts, f, indent=2, ensure_ascii=False)

print(f"Converted {len(posts)} posts -> {JSON_FILE}")
# Now generate HTML files for each post (using template file post-template.html)
template = open("post-template.html","r",encoding="utf-8").read() if os.path.exists("post-template.html") else "{body}"
os.makedirs(OUTPUT_DIR, exist_ok=True)
for p in posts:
    html_out = template.replace("{title}", p["title"]).replace("{body}", p["body"]).replace("{date}", p["date"])
    open(os.path.join(OUTPUT_DIR, os.path.basename(p["url"])), "w", encoding="utf-8").write(html_out)

print("Done. Upload posts/ and posts.json to GitHub.")
