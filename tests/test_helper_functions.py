# tests/test_helper_functions.py
import unittest
from src.util import filter_recipe_link, format_link


class TestHelperFunctions(unittest.TestCase):
    def test_filter_recipe_link(self):
        self.assertTrue(filter_recipe_link("https://www.epicurious.com/recipes/food/views/philly-fluff-cake"))
        self.assertFalse(filter_recipe_link("/non-recipe-link"))

    def test_format_link(self):
        self.assertEqual(format_link("/recipes/food/views/test-recipe"),
                         "https://www.epicurious.com/recipes/food/views/test-recipe")
        self.assertEqual(format_link("recipes/food/views/test-recipe"),
                         "https://www.epicurious.com/recipes/food/views/test-recipe")
        self.assertEqual(format_link("https://www.epicurious.com/recipes/food/views/test-recipe"),
                         "https://www.epicurious.com/recipes/food/views/test-recipe")


if __name__ == '__main__':
    unittest.main()
