from tech_news.database import get_collection


# Requisito 10
def top_5_news():
    query_result = (
        get_collection()
        .find({}, {"_id": 0})
        .sort([("comments_count", -1), ("title", 1)])
        .limit(5)
    )
    posts = list(query_result)

    return [(post["title"], post["url"]) for post in posts]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
