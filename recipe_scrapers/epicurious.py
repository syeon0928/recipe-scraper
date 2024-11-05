from ._abstract import AbstractScraper
from ._utils import normalize_string


class Epicurious(AbstractScraper):

    @classmethod
    def host(self):
        return 'epicurious.com'

    def head(self):
        return self.soup.find('title')

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
        recipe_photo = self.soup.find('div', {'class': "recipe-image-container"}).find('img')
        return recipe_photo['srcset']

    def tags(self):
        tag_cloud_div = self.soup.find('div', {'data-testid': 'TagCloudWrapper'})
        if tag_cloud_div:
            tags = [
                {
                    'tag': tag.find('span').get_text().strip(),
                    'category': tag['href'].strip('/').split('/')[0],
                    'link': tag['href'],
                }
                for tag in tag_cloud_div.find_all('a', href=True)  # Only get <a> tags with href
                if tag.find('span')  # Ensure there's a <span> for the tag name
            ]

if __name__ == '__main__':
    pass
