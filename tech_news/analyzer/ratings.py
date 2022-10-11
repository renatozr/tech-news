from tech_news.database import get_collection, find_news


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
    posts = find_news()

    categories_count = {}

    for post in posts:
        category = post["category"]
        if category not in categories_count.keys():
            categories_count[category] = 0
        categories_count[category] += 1

    categories_count_sorted = sorted(
        categories_count.items(), key=lambda x: (-x[1], x[0])
    )

    return [category_count[0] for category_count in categories_count_sorted]
