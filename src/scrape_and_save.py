import json
import os
from recipe_scrapers import scrap_me


# Scrape individual recipe information using scrap_me function
def get_recipe(url):
    try:
        scraper = scrap_me(url)
        return {
            'title': scraper.title(),
            'ingredients': scraper.ingredients(),
            'instructions': scraper.instructions(),
            'picture_link': scraper.picture() if hasattr(scraper, 'picture') else None,
            'cooking_time': scraper.total_time(),
            'servings': scraper.servings(),
            'ratings': scraper.ratings(),
            'tags': scraper.tags(),
            'author': scraper.author(),
            'publish_date': scraper.publish_date()

        }
    except Exception as e:
        print(f"Could not scrape URL {url}: {e}")
        return {}

