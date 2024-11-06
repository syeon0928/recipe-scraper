# main.py
from src.config import *
from src.gather_urls import get_recipe_links_from_menu, get_recipe_links_from_list, get_all_recipe_links
from db.recipe_url_storage import load_links, save_links


def scrape_all_recipe_urls_from_menu():
    # from the cnofig.recipe menu dictionary
    all_links = load_links()

    # Scrape from recipe menus
    for menu_key, menu_path in recipe_menus.items():
        print(f"Scraping menu: {menu_key}")
        links = get_recipe_links_from_menu(menu_path)
        all_links.update(links)

    save_links(all_links)
    print(f"Scraping completed. Total recipes collected: {len(all_links)}")


def scrape_all_recipe_urls_from_list():
    # from the config.recipe_list
    all_links = load_links()

    # Scrape from paginated recipe lists
    for list_path in recipe_lists:
        print(f"Scraping list: {list_path}")
        links = get_recipe_links_from_list(list_path)
        all_links.update(links)

    save_links(all_links)
    print(f"Scraping completed. Total recipes collected: {len(all_links)}")


def scrape_all_recipe_urls_from_search():
    # from the website search site
    all_links = load_links()

    # Scrape from search list
    links = get_all_recipe_links()
    all_links.update(links)

    save_links(all_links)
    print(f"Scraping completed. Total recipes collected: {len(all_links)}")


def scrape_all_recipes():
    return None


if __name__ == '__main__':
    # scrape_all_recipe_urls_from_menu()
    # scrape_all_recipe_urls_from_list()
    scrape_all_recipe_urls_from_search()