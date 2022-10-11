import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def insert_news_in_db_option():
    news_amount = input("Digite quantas notícias serão buscadas:")
    get_tech_news(news_amount)


def find_news_by_title_option():
    title = input("Digite o título:")
    print(search_by_title(title))


def find_news_by_date_option():
    date = input("Digite a data no formato aaaa-mm-dd:")
    print(search_by_date(date))


def find_news_by_tag_option():
    tag = input("Digite a tag:")
    print(search_by_tag(tag))


def find_news_by_category_option():
    category = input("Digite a categoria:")
    print(search_by_category(category))


def list_top_5_news_option():
    print(top_5_news())


def list_top_5_categories_option():
    print(top_5_categories())


def exit_option():
    print("Encerrando script\n")


# Requisito 12
def analyzer_menu():
    option = input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair."""
    )

    menu_options = {
        "0": insert_news_in_db_option,
        "1": find_news_by_title_option,
        "2": find_news_by_date_option,
        "3": find_news_by_tag_option,
        "4": find_news_by_category_option,
        "5": list_top_5_news_option,
        "6": list_top_5_categories_option,
        "7": exit_option,
    }

    try:
        menu_options[option]()
    except KeyError:
        print("Opção inválida", file=sys.stderr)
