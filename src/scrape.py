import json
import os
from recipe_scrapers import scrap_me


# Scrape individual recipe information using scrap_me function
def get_recipe(url):
    try:
        scraper = scrap_me(url)
        return {
            'url': url,
            'title': scraper.title(),
            'description' : scraper.description() if hasattr(scraper, 'description') else None,
            'ingredients': scraper.ingredients(),
            'instructions': scraper.instructions(),
            'picture_link': scraper.picture() if hasattr(scraper, 'picture') else None,
            'cooking_time': scraper.total_time(),
            'servings': scraper.servings() if hasattr(scraper, 'servings') else None,
            'ratings': scraper.ratings() if hasattr(scraper, 'ratings') else None,
            'tags': scraper.tags() if hasattr(scraper, 'tags') else None,
            'author': scraper.author() if hasattr(scraper, 'author') else None,
            'publish_date': scraper.publish_date() if hasattr(scraper, 'publish_date') else None

        }
    except Exception as e:
        print(f"Could not scrape URL {url}: {e}")
        return {}

