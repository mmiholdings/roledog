import feedparser, json, csv, os

feeds = {
    "HackerNews": "https://news.ycombinator.com/rss",
    "RedditMovies": "https://www.reddit.com/r/movies/.rss",
    "RedditTV": "https://www.reddit.com/r/television/.rss",
    "RedditEntertainment": "https://www.reddit.com/r/entertainment/.rss",
    "RedditScreenwriting": "https://www.reddit.com/r/Screenwriting/.rss"
}

os.makedirs("data", exist_ok=True)

all_posts = []

for name, url in feeds.items():
    print(f"\n--- {name} ({url}) ---")
    parsed = feedparser.parse(url)
    items = []

    for entry in parsed.entries[:10]:
        title = entry.title
        link = entry.link
        summary = getattr(entry, 'summary', '')
        print(f"{title} — {link}")
        items.append({
            "source": name,
            "title": title,
            "link": link,
            "summary": summary
        })
        all_posts.append({
            "Source": name,
            "Title": title,
            "Link": link,
            "Summary": summary
        })

    with open(f"data/{name.lower()}.json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

with open("data/all_entertainment_posts.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=["Source", "Title", "Link", "Summary"])
    writer.writeheader()
    writer.writerows(all_posts)
