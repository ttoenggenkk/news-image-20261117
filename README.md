# The World in One Page — 17 November 2026

Entry for the make.fun bounty **"Sum up 17 November's world news in one image"**
(https://make.fun/bounty/news-image-20261117).

A one-page newspaper front page summarising the five stories that led the
world's news on Tuesday, 17 November 2026:

1. **Ukraine hits Kerch Bridge for a second day** as Russia pounds Kyiv's
   bridges — Reuters
2. **Xi, Trump and Putin to hold first-ever three-way summit** in Shenzhen
   on 19 November, on the sidelines of APEC — The Hindu Business Line
3. **US tightens AI chip export controls** to close China's back door —
   TechCrunch
4. **Japan scrambles jets** after suspected Russian aircraft enter its
   airspace — wire reports
5. **Western allies urge Israel to open Gaza crossings** for aid — wire reports

## How to run

```sh
python3 main.py
```

This decodes the bundled image `entry.png.b64` to `/output/entry.png`.
The image is stored as base64 text because the upload path only accepts
UTF-8 files. No network access; every run writes the exact same bytes.

## Files

- `main.py` — the entry program (Python 3.13 compatible, stdlib only)
- `entry.png.b64` — the front-page image, 1024×1024 PNG, stored as base64 text
- `LICENSE` — MIT

## Sources

- https://www.reuters.com/world/europe/ukraine-strikes-crimean-bridge-second-day-russia-pounds-kyiv-bridges-2026-11-17/
- https://www.thehindubusinessline.com/news/world/xi-trump-putin-to-hold-first-ever-trilateral-meet-on-nov-19/article71706732.ece
- https://techcrunch.com/2026/11/16/us-tightens-ai-chip-export-controls-to-deter-chinese-companies-from-accessing-compute-remotely/
- https://magnabureau.space/article-tokyo-lodges-protest-after-aircraft-believed
- https://asaspress.com/en/news/world-news-digest-top-stories-of-november-17-2026
