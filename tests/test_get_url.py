# tests/test_gather_urls.py
import unittest
from src.gather_urls import *


class TestScraper(unittest.TestCase):
    def test_get_recipe_links_from_menu(self):
        links = get_recipe_links_from_menu("recipes-menus/most-popular-recipes-gallery")
        self.assertIsInstance(links, list)

    def test_get_recipe_links_from_list(self):
        links = get_recipe_links_from_list("ingredient/broccoli")
        self.assertIsInstance(links, list)

    def test_get_all_recipes(self):
        self.assertIsInstance(get_all_recipe_links(), list)


if __name__ == '__main__':
    unittest.main()
