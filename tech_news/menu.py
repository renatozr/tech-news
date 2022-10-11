import sys


def insert_news_in_db_option():
    input("Digite quantas notícias serão buscadas:")


def find_news_by_title_option():
    input("Digite o título:")


def find_news_by_date_option():
    input("Digite a data no formato aaaa-mm-dd:")


def find_news_by_tag_option():
    input("Digite a tag:")


def find_news_by_category_option():
    input("Digite a categoria:")


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
        0: insert_news_in_db_option,
        1: find_news_by_title_option,
        2: find_news_by_date_option,
        3: find_news_by_tag_option,
        4: find_news_by_category_option,
    }

    try:
        menu_options[option]()
    except KeyError:
        print("Opção inválida", file=sys.stderr)
