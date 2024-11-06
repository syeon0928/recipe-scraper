from ._abstract import AbstractScraper
from ._utils import normalize_string, get_minutes, get_servings
import re



class Epicurious(AbstractScraper):

    @classmethod
    def host(self):
        return 'epicurious.com'

    def title(self):
        return self.soup.find('h1', {'data-testid': 'ContentHeaderHed'}).get_text().strip()

    def total_time(self):
        info_items = self.soup.find_all('li', class_="InfoSliceListItem-hNmIoI cmiFLD")
        # Loop through each item to find Total Time
        for item in info_items:
            # Find the key and value text in each item
            key = item.find('p', class_="InfoSliceKey-gHIvng").get_text(strip=True)

            # Check if the key matches "Total Time"
            if key == "Total Time":
                total_time = item.find('p', class_="InfoSliceValue-tfmqg")
                return get_minutes(total_time)
        else:
            return None

    def ingredients(self):
        ingredients_container = self.soup.find('div', {'data-testid': 'IngredientList'})

        if not ingredients_container:
            return None

        # Find all ingredient items within the container
        ingredient_items = ingredients_container.find_all('div', class_="BaseWrap-sc-gjQpdd BaseText-ewhhUZ Description-cSrMCf iUEiRd bGCtOd fsKnGI")

        # Extract text from each ingredient item, cleaning up whitespace and newlines
        ingredients = []
        for item in ingredient_items:
            text = item.get_text().strip()

            # Ignore items containing "Equipment:"
            if "Equipment:" in text:
                continue

            ingredients.append(text)

        return ingredients

    def instructions(self):
        instructions_container = self.soup.find('div', {'data-testid': 'InstructionsWrapper'})

        if not instructions_container:
            return None

        # Find all instruction paragraphs within the ordered list
        instruction_steps = instructions_container.find_all('p')

        # Extract the text for each step
        instructions = [re.split(r'\n', step.get_text().strip())[0] for step in instruction_steps]
        return {i+1: instructions[i] for i in range(len(instructions))}

    def picture(self):
        recipe_photo = self.soup.find_all('img', class_="ResponsiveImageContainer-eybHBd fptoWY responsive-image__image")
        if not recipe_photo:
            return None
        return recipe_photo[2]['src']

    def tags(self):
        tag_cloud_div = self.soup.find('div', {'data-testid': 'TagCloudWrapper'})

        if not tag_cloud_div:
            return None

        tagging = [
            {
                'tag': tag.find('span').get_text().strip(),
                'category': tag['href'].strip('/').split('/')[0],
            }
            for tag in tag_cloud_div.find_all('a', href=True)  # Only get <a> tags with href
        ]
        return tagging

    def servings(self):
        info_items = self.soup.find_all('li', class_="InfoSliceListItem-hNmIoI cmiFLD")
        # Loop through each item to find servings
        for item in info_items:
            # Find the key and value text in each item
            key = item.find('p', class_="InfoSliceKey-gHIvng").get_text(strip=True)

            if key == "Yield":
                serving_amount = item.find('p', class_="InfoSliceValue-tfmqg")
                return get_servings(serving_amount)

        return None

    def ratings(self):
        ratings_div = self.soup.find('div', {'href': '#reviews'})
        ratings = ratings_div.find_all('p')
        if not ratings:
            return None
        return {'rating': float(ratings[0].get_text()), 'count': int(re.findall(r'\d+', ratings[1].get_text())[0])}

    def author(self):
        # Find all <a> tags where href contains 'contributors/' followed by any text
        contributor = self.soup.find('a', href=re.compile(r'/contributors/.*'))

        if not contributor:
            return None

        return contributor.get_text().strip()

    def publish_date(self):
        publish_date = self.soup.find('time', {'data-testid': 'ContentHeaderPublishDate'})
        if not publish_date:
            return None
        return publish_date.get_text().strip()
