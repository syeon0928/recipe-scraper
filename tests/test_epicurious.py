import os
import unittest

from recipe_scrapers.epicurious import Epicurious
from recipe_scrapers import scrap_me


class TestEpicurious(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        # with open('test_data/epicurious.html') as file_opened:
        #     self.harvester_class = Epicurious(file_opened, test=True)
        # url="https://www.epicurious.com/recipes/food/views/spicy-sichuan-tofu-em-mapo-doufu-em-242878"
        url ="https://www.epicurious.com/recipes/food/views/blt-soup-385105"
        self.harvester_class = scrap_me(url)

    def test_host(self):
        self.assertEqual(
            'epicurious.com',
            self.harvester_class.host()
        )

    def test_title(self):
        # self.assertEqual(
        #     'Mapo Tofu (麻婆豆腐)',
        #     self.harvester_class.title()
        # )
        print('Title: ', self.harvester_class.title())

    def test_total_time(self):
        # self.assertEqual(
        #     25,
        #     self.harvester_class.total_time()
        # )
        print('Time: ', self.harvester_class.total_time())

    def test_servings(self):
        # self.assertEqual(
        #     4,
        #     self.harvester_class.servings()
        # )
        print('Servings: ', self.harvester_class.servings())

    def test_ingredients(self):
        # self.assertListEqual(
        #     ['½ teaspoon Sichuan peppercorns, toasted and cooled',
        #      '1 (14- to 17-ounce) package tofu (not silken), rinsed',
        #      '3 tablespoons peanut or vegetable oil',
        #      '5 ounces ground pork butt (not lean; ⅔ cup)',
        #      '2½ tablespoons toban jiang (hot bean sauce)',
        #      '1 tablespoon fermented black beans, rinsed, drained, and chopped',
        #      '2 teaspoons Sichuan chili powder',
        #      '1 cup chicken stock or reduced-sodium chicken broth',
        #      '2 teaspoon soy sauce',
        #      '1 teaspoon sugar',
        #      '1 tablespoons cornstarch',
        #      '4 teaspoons water',
        #      '4 scallions, chopped (½ cup)',
        #      ],
        #     self.harvester_class.ingredients()
        # )
        print('Ingredients: ', self.harvester_class.ingredients())

    def test_instructions(self):
        # return self.assertEqual(
        #     {1: 'Grind peppercorns in grinder and set aside.',
        #      2: 'Cut tofu into ¾-inch cubes and pat dry.',
        #      3: 'Heat wok over high heat until it begins to smoke, then pour oil down side and swirl to coat bottom and side. Stir-fry pork until no longer pink. Add bean sauce, black beans, and chile powder and stir-fry 1 minute. Stir in stock, soy sauce, sugar, tofu, and a pinch of salt. Simmer, gently stirring occasionally, 5 minutes.',
        #      4: 'Meanwhile, stir together cornstarch and water until smooth.',
        #      5: 'Stir cornstarch slurry mixture into stir-fry and simmer, gently stirring occasionally, 1 minute. Stir in scallions and simmer 1 minute. Serve sprinkled with Sichuan pepper.',
        #      6: 'Serve with rice.'},
        #     self.harvester_class.instructions()
        # )
        print('Instructions: ', self.harvester_class.instructions())

    def test_images(self):
        # return self.assertEqual(
        #     'https://assets.epicurious.com/photos/624b45cc1184c47f7e94b17e/1:1/w_2560%2Cc_limit/MapoTofu_RECIPE_033122_31225.jpg',
        #     self.harvester_class.picture()
        # )
        print('Image Link: ', self.harvester_class.picture())

    def test_ratings(self):
        # return self.assertEqual(
        #     {'rating': 4.6, 'count': 13},
        #     self.harvester_class.ratings()
        # )
        print('Ratings: ', self.harvester_class.ratings())

    def test_author(self):
        # return self.assertEqual(
        #     'Eileen Wen Mooney',
        #     self.harvester_class.author()
        # )
        print('Author: ', self.harvester_class.author())

    def test_publish_date(self):
        # return self.assertEqual(
        #     'April 11, 2022',
        #     self.harvester_class.publish_date()
        # )
        print('Publish date: ', self.harvester_class.publish_date())

    def test_description(self):
        desc = self.harvester_class.description()
        print('Description: ', desc)

    def test_tags(self):
        tags = self.harvester_class.tags()
        print('Tags: ', tags)


if __name__ == '__main__':
    unittest.main()
