import sys
from urllib.error import HTTPError, URLError
from urllib import request
from bs4 import BeautifulSoup
import ssl
import os
import certifi

# Add the `src` directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from config import BASE_URL, HEADERS
from util import *


def get_soup(url):
    """Fetches the HTML content and returns a BeautifulSoup object."""
    try:
        context = ssl.create_default_context(cafile=certifi.where())
        response = request.urlopen(request.Request(url, headers=HEADERS), context=context)
        return BeautifulSoup(response.read(), "html.parser", from_encoding="utf-8")

    except URLError as e:
        print(f"URL error fetching {url}: {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred while fetching {url}: {e}")
    return None


def save_soup_as_html(soup, filename="soup_response.html"):
    """Saves the BeautifulSoup object as an HTML file for inspection."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(soup))
    print(f"HTML content saved to {os.path.abspath(filename)}")


def get_all_recipe_links():
    links = []
    page = 1
    while True:
        print(f"Searching page {page}")
        url = f"{BASE_URL}search?q=&content=recipe&p={page}"
        soup = get_soup(url)
        if not soup:
            print("No more pages found or unable to fetch page.")
            break

        summary_collection = soup.find("div", {'data-testid': "SummaryCollectionGridItems"})
        clamp_wrapper = summary_collection.find_all("div", {'data-testid': "ClampWrapper"})
        for item in clamp_wrapper:
            item_a = item.find("a")
            if item_a:
                link = format_link(item.find("a")['href'])
                if filter_recipe_link(link):
                    links.append(link)
        page += 1
    return links


def get_recipe_links_from_menu(menu_path):
    """Extract recipe links from a given menu page (without pagination)."""
    url = f"{format_link(menu_path)}"
    soup_menu = get_soup(url)
    if not soup_menu:
        return []

    links = []
    for btn in soup_menu.find_all('a', {'data-testid': 'Button'}):
        span_text = btn.find('span').get_text() if btn.find('span') else ""
        if span_text == 'Get This Recipe':
            link = format_link(btn['href'])
            if filter_recipe_link(link):
                links.append(link)
    return links


def get_recipe_links_from_list(list_path):
    """Extract recipe links from a paginated list."""
    links = []
    page = 1

    while True:
        print(f"Searching page {page}")
        url = f"{format_link(list_path)}?page={page}"
        soup = get_soup(url)
        if not soup:
            print("No more pages found or unable to fetch page.")
            break

        # Find all items in the summary list
        items = soup.find_all('div', class_='summary-list__items')
        if not items:
            print("No items found on this page. Ending pagination.")
            break

        # Extract links from each item
        for item in items:
            for link in item.find_all('a', href=True):
                href = format_link(link['href'])
                if filter_recipe_link(href):
                    links.append(href)
                else:
                    # Call get_recipe_links_from_menu if link doesn't pass the filter
                    menu_links = get_recipe_links_from_menu(href)
                    links.extend(menu_links)

        page += 1
    return links
