import requests
import time
from parsel import Selector


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
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
