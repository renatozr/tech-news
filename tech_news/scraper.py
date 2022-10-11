import requests
import time
from parsel import Selector
import re


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        res = requests.get(
            url,
            header={"user-agent": "Fake user-agent"},
            timeout=3,
        )
    except requests.ReadTimeout:
        return None

    if res.status_code == 200:
        return res.text
    else:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)

    news_urls = selector.css("h2.entry-title a::attr(href)").getall()

    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    next_page_url = selector.css("a.next::attr(href)").get()

    return next_page_url


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    url = selector.css("head link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author a::text").get()
    comments = selector.css("ol.comment-list li").getall()
    # ref:
    # https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
    re_htmltags = re.compile(r"<[^>]+>")
    summary = re_htmltags.sub("", selector.css("div.entry-content p").get())
    tags = selector.css(".post-tags a::text").getall()
    category = selector.css(".meta-category span.label::text").get()

    news = {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": len(comments),
        "summary": summary.strip(),
        "tags": tags,
        "category": category,
    }

    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
