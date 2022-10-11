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
    posts = search_news({"tags": {"$regex": tag, "$options": "i"}})

    return [(post["title"], post["url"]) for post in posts]


# Requisito 9
def search_by_category(category):
    posts = search_news({"category": {"$regex": category, "$options": "i"}})

    return [(post["title"], post["url"]) for post in posts]
