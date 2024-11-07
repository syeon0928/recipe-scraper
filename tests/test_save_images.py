# tests/test_gather_urls.py
import unittest
from db.save_images import *
from config import *


class TestCaseBase(unittest.TestCase):
    def assertIsFile(self, path):
        if not os.path.isfile(path):
            raise AssertionError("File does not exist: %s" % str(path))


class TestSaveImages(TestCaseBase):
    def setUp(self):
        self.recipe_url = 'https://www.epicurious.com/recipes/food/views/artichoke-and-bean-bruschetta-386837'
        self.image_url = 'https://assets.epicurious.com/photos/600213bbe1a77f3b0c16bdd2/16:9/w_2580%2Cc_limit/MushroomTacos_HERO_011421_7171_VOG_final.jpg'
        self.test_recipes = [{
        "url": "https://www.epicurious.com/recipes/food/views/mutabal-51231810",
        "title": "Mutabal",
        "picture_link": "https://assets.epicurious.com/photos/54ac97ed19925f464b3ac7ea/1:1/w_2560%2Cc_limit/51231810_mutabal_1x1.jpg",
    },]

    def test_extract_file_name(self):
        self.assertEqual(extract_filename(self.recipe_url), 'artichoke-and-bean-bruschetta-386837')

    def test_save_image_locally(self):
        save_image_locally('test', self.image_url)
        self.assertIsFile(os.path.join(IMAGE_FOLDER_PATH, 'test.jpg'))

    def test_main(self):
        main(test_recipes=self.test_recipes)


if __name__ == '__main__':
    unittest.main()