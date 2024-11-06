import json
import time
from urllib import request
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import argparse
from os import path
import sys
from recipe_scrapers import scrap_me

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
}


# Scrape individual recipe information using scrap_me function
def get_recipe(url):
    try:
        scraper = scrap_me(url)
        return {
            'title': scraper.title(),
            'ingredients': scraper.ingredients(),
            'instructions': scraper.instructions(),
            'picture_link': scraper.picture() if hasattr(scraper, 'picture') else None,

        }
    except Exception as e:
        print(f"Could not scrape URL {url}: {e}")
        return {}


# Gather all Epicurious recipe URLs from paginated search results
def get_all_recipes_epi(page_num):
    base_url = 'https://www.epicurious.com'
    search_url_str = 'search/?content=recipe&page'
    url = f"{base_url}/{search_url_str}={page_num}"

    try:
        # Fetch and parse the page
        soup = BeautifulSoup(request.urlopen(
            request.Request(url, headers=HEADERS)).read(), "html.parser")
        recipe_link_items = soup.select('div.results-group article.recipe-content-card a.view-complete-item')

        # Extract recipe links and remove duplicates
        recipe_links = list(set([base_url + r['href'] for r in recipe_link_items]))
        return {link: get_recipe(link) for link in recipe_links}
    except (HTTPError, URLError) as e:
        print(f"Could not parse page {url}: {e}")
        return {}


# Save recipes to JSON file for persistence
def save_recipes(filename, recipes):
    with open(filename, 'w') as f:
        json.dump(recipes, f, indent=4)


# Main function to orchestrate scraping for Epicurious
def scrape_recipes(start_page, num_pages, sleep_interval=1, status_interval=5, append=False):
    # Load existing recipes if appending
    if append and path.exists('recipes_epicurious.json'):
        with open('recipes_epicurious.json', 'r') as f:
            all_recipes = json.load(f)
    else:
        all_recipes = {}

    for page in range(start_page, start_page + num_pages):
        print(f"Scraping page {page}")
        new_recipes = get_all_recipes_epi(page)
        all_recipes.update(new_recipes)

        # Save progress intermittently and print status
        if page % status_interval == 0:
            save_recipes('recipes_epicurious.json', all_recipes)
            print(f"Saved progress after scraping page {page}")

        time.sleep(sleep_interval)  # Respectful delay between requests

    # Final save after completing all pages
    save_recipes('recipes_epicurious.json', all_recipes)
    print(f"Scraping completed! Total recipes scraped: {len(all_recipes)}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Epicurious Recipe Scraper")
    parser.add_argument('--start', type=int, default=1, help='Starting page number')
    parser.add_argument('--pages', type=int, default=10, help='Number of pages to scrape')
    parser.add_argument('--sleep', type=int, default=1, help='Seconds to wait between page requests')
    parser.add_argument('--status', type=int, default=5, help='Interval of pages to save progress')
    parser.add_argument('--append', action='store_true', help='Append to existing JSON data')

    args = parser.parse_args()
    scrape_recipes(args.start, args.pages, args.sleep, args.status, args.append)
