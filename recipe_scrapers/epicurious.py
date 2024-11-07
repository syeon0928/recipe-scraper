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
        if not info_items:
            return None

        # Loop through each item to find Total Time
        for item in info_items:
            # Find the key and value text in each item
            key = item.find('p', class_="InfoSliceKey-gHIvng").get_text(strip=True)

            # Check if the key matches "Total Time"
            if key == "Total Time":
                total_time = item.find('p', class_="InfoSliceValue-tfmqg")
                return get_minutes(total_time)

    def ingredients(self):
        ingredients_container = self.soup.find('div', {'data-testid': 'IngredientList'})

        if not ingredients_container:
            return None

        # Find all ingredient items within the container
        ingredient_items = ingredients_container.find_all('div',
                                                          class_="BaseWrap-sc-gjQpdd BaseText-ewhhUZ Description-cSrMCf iUEiRd bGCtOd fsKnGI")

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
        return {i + 1: instructions[i] for i in range(len(instructions))}

    def picture(self):
        # recipe_photo = self.soup.find_all('img',
        #                                   c)
        # if not recipe_photo:
        #     return None
        # return recipe_photo[2]['src']

        recipe_image_div = self.soup.find('div', {'data-testid': 'ContentHeaderLeadAsset'})
        if not recipe_image_div:
            return None
        image_found = recipe_image_div.find('img', class_="ResponsiveImageContainer-eybHBd fptoWY responsive-image__image")
        return image_found.get('src')

    def tags(self):
        tag_cloud_div = self.soup.find('div', {'data-testid': 'TagCloudWrapper'})

        if not tag_cloud_div:
            return None

        # Initialize a dictionary to group tags by category
        tagging = {}
        for tag in tag_cloud_div.find_all('a', href=True):  # Only get <a> tags with href
            category = tag['href'].strip('/').split('/')[0]
            tag_name = tag.find('span').get_text().strip()

            # Append tag to the category list; create the list if it doesn't exist
            if category in tagging:
                tagging[category].append(tag_name)
            else:
                tagging[category] = [tag_name]

        return tagging

    def servings(self):
        info_items = self.soup.find_all('li', class_="InfoSliceListItem-hNmIoI cmiFLD")
        if not info_items:
            return None

        # Loop through each item to find servings
        for item in info_items:
            # Find the key and value text in each item
            key = item.find('p', class_="InfoSliceKey-gHIvng").get_text(strip=True)

            if key == "Yield":
                serving_amount = item.find('p', class_="InfoSliceValue-tfmqg")
                return get_servings(serving_amount)

    def ratings(self):
        ratings_div = self.soup.find('div', {'href': '#reviews'})
        if not ratings_div:
            return None

        ratings = ratings_div.find_all('p')
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

    def description(self):
        box = self.soup.find('div', {'data-testid': 'BodyWrapper'})
        if not box:
            return None
        texts = [p.get_text(" ", strip=True) for p in box.find_all("p")]

        # Join each paragraph's text into a single string
        combined_text = "\n".join(texts)

        return combined_text
