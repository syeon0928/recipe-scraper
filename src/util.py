from config import BASE_URL, RECIPE_URL
import os
from urllib.parse import urljoin


def filter_recipe_link(link):
    """Returns True if the link is a valid recipe link."""
    return link.startswith(f'{BASE_URL}{RECIPE_URL}')


def format_link(link):
    """Formats link by adding or removing the base URL as needed."""
    return urljoin(BASE_URL, link)
