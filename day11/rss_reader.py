import feedparser

def fetch_rss_feed(url):
    return feedparser.parse(url)

def display_feed(feed):
    print('フィード:' + feed.feed.title)
    for entry in feed.entries:
        print("タイトル：",entry.title)
        print("リンク：",entry.link)
        print()

def main():
    rss_url = "http://feeds.bbci.co.uk/news/rss.xml"  # ここに他のRSSフィードURLを使用することも可能
    feed = fetch_rss_feed(rss_url)
    display_feed(feed)


if __name__ == "__main__":
    main()