from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    posts = search_news({"title": {"$regex": title, "$options": "i"}})

    return [(post["title"], post["url"]) for post in posts]


# Requisito 7
def search_by_date(date):
    try:
        posts = search_news(
            {
                "timestamp": datetime.date.fromisoformat(date).strftime(
                    "%d/%m/%Y"
                )
            }
        )
    except ValueError:
        raise ValueError("Data inválida")

    return [(post["title"], post["url"]) for post in posts]


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
