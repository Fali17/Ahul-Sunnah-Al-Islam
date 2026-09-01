
# Ahlu-Sunnah Al Islam - GitHub Pages Migration

This is your Blogger template converted to a GitHub Pages static site.

## Structure
- `index.html` - Homepage that loads posts from `posts.json`
- `assets/css/style.css` - Your exact Blogger CSS (green theme)
- `assets/js/main.js` - Mobile menu, back-to-top, reading progress, and prev/next logic
- `posts/` - Individual post HTML files
- `posts.json` - List of all posts (used for homepage, popular, and prev/next)
- `blogger_to_github.py` - Script to convert your real Blogger export

## How to do 1) Replace placeholder posts with real posts

**Option A - Automatic (Recommended):**
1. Go to Blogger Dashboard > Settings > Manage Blog > Back up content > Download -> you get `blog-...xml`
2. Put that file in this folder as `blog-01-01-2024.xml`
3. Copy one of the sample posts in `posts/` as `post-template.html` and put `{title}`, `{date}`, `{body}` placeholders
4. Run: `python blogger_to_github.py`
5. It creates `posts.json` and all `posts/*.html` with your real content, preserving formatting/images.

**Option B - Manual:**
- Edit `posts.json` - add your post objects with title, url, date, snippet, body
- Copy `posts/following-the-sunnah.html` as template, replace body

## How to do 2) Single post prev/next on GitHub Pages

Original Blogger template used `/feeds/posts/default?alt=json` which doesn't work on GitHub.

This version fixes it:
- `assets/js/main.js` has `initPostNav()` that fetches `/posts.json`
- Finds current post index and injects Previous/Next buttons with titles
- Works offline/static, no Blogger API needed.

Each single post file has: `<div class="post-nav" id="postNav"></div>` - JS fills it.

## Deploy to GitHub Pages

1. Create new repo on GitHub: e.g. `ahlu-sunnah-al-islam` or `YOURUSERNAME.github.io`
2. Upload all files in this folder to repo (drag & drop)
3. Go to repo Settings > Pages > Source: Deploy from branch, Branch: main, Folder: / (root)
4. Save. Wait 1-2 mins. Your site will be at `https://YOURUSERNAME.github.io/ahlu-sunnah-al-islam/` or `https://YOURUSERNAME.github.io/`

**Custom domain:** Settings > Pages > Custom domain > add `ahlusunnahalislam.com` etc, then add CNAME record in your domain DNS.

**Images:** Blogger images will still work (blogger.googleusercontent.com). For best performance, download them and put in `assets/images/`.

Need me to convert your real export? Upload your `blog-....xml` backup file here and I'll generate the full site.
