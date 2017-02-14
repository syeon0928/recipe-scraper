from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class Epicurious(AbstractScraper):

    @classmethod
    def host(self):
        return 'epicurious.com'

    def title(self):
        return self.soup.find('h1', {'itemprop': 'name'}).get_text()

    def total_time(self):
        return -1

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'itemprop': "ingredients"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.find('ol', {'class': 'preparation-groups'}).find_all('li')

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])

    def picture(self):
        recipe_photos = self.soup.find('div', {'class': "recipe-image-container"}).find_all('img')
        return [recipe_photo['srcset'] for recipe_photo in recipe_photos]
