# main.py
from src.gather_urls import *
from src.scrape import get_recipe
from db.json_db import *
# from db.mongo_db import *
import argparse
from db.save_images import *


def scrape_all_recipe_urls_from_menu():
    # from the cnofig.recipe menu dictionary
    all_links = load_json_to_set()

    # Scrape from recipe menus
    for menu_key, menu_path in recipe_menus.items():
        print(f"Scraping menu: {menu_key}")
        links = get_recipe_links_from_menu(menu_path)
        all_links.update(links)

    # Scrape from paginated recipe lists
    for list_path in recipe_lists:
        print(f"Scraping list: {list_path}")
        links = get_recipe_links_from_list(list_path)
        all_links.update(links)

    save_to_json(all_links)
    print(f"Scraping completed. Total recipes collected: {len(all_links)}")


def scrape_all_recipe_urls_from_search():
    # from the website search site
    all_links = load_json_to_set()

    # Scrape from search list
    links = get_all_recipe_links()
    all_links.update(links)

    save_to_json(all_links)
    print(f"Scraping completed. Total recipes collected: {len(all_links)}")


def json_db():
    # Load URLs from JSON file
    urls_to_scrape = load_json_to_set()
    # Load existing scraped recipes
    all_recipes = load_json_to_list()
    # Check already scraped urls
    scraped_urls = {recipe['url'] for recipe in all_recipes}
    # filter already scraped urls
    urls_to_scrape = urls_to_scrape - scraped_urls

    print(f'{len(urls_to_scrape)} more recipes to scrape!')

    # Process each URL: scrape and save to MongoDB
    for i, url in enumerate(urls_to_scrape):
        # scrape for the url
        recipe_data = get_recipe(url)

        # append if data exists
        if recipe_data:
            all_recipes.append(recipe_data)
            print(i, recipe_data)
        else:
            print(f'Failed to save: {url}')

        # progress checking
        if i % 100 == 0:
            save_to_json(all_recipes, filename=f'db/{RECIPES_FILE_PATH}')  # save to the file in case of disruption
            print(f"Save Points: {len(all_recipes)} saved to the file.")

    # Save all the recipes to json file
    print(f'Total recipes collected: {len(all_recipes)}')
    save_to_json(all_recipes, filename=f'db/{RECIPES_FILE_PATH}')


def mongo_db():
    return None


def main(db):
    scrape_all_recipe_urls_from_search()
    if db == 'json':
        json_db()
    if db == 'mongo':
        mongo_db()
    save_all_images()


if __name__ == '__main__':
    if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('--db', type=str, default='json',
                            help='--mongo for using mongodb, make sure you have MONGO_URI in .env')
        args = parser.parse_args()
        main(args.db)
