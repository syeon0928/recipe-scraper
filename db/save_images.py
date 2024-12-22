import certifi
import ssl
from os import path
from urllib import request
import config
from db.json_db import *


def extract_filename(url):
    return url.split('/')[-1]


def save_image_locally(file_name, img_url):
    path_save = path.join(
        os.path.abspath(config.IMAGE_FOLDER_PATH), '{}.jpg'.format(file_name))

    # set up ssl certificates
    context = ssl.create_default_context(cafile=certifi.where())

    try:
        # request.urlretrieve(img_url, path_save)
        response = request.urlopen(request.Request(img_url, headers=HEADERS), context=context)
        image_data = response.read()

        # Write the image data to a file
        with open(path_save, 'wb') as out_file:
            out_file.write(image_data)

    except Exception as e:
        print('Could not download image from {}.'.format(img_url))
        print(f'Error message: {e}')


def update_recipes(all_recipes):
    """Update recipes by removing URL fields and adding image filenames."""
    updated_recipes = []
    for recipe in all_recipes:
        recipe_copy = recipe.copy()  # Avoid modifying the original
        image_filename = extract_filename(recipe['url'])
        recipe_copy['image_filename'] = image_filename
        recipe_copy.pop('url', None)  # Remove 'url'
        recipe_copy.pop('picture_link', None)  # Remove 'picture_link'
        updated_recipes.append(recipe_copy)
    return updated_recipes


def save_all_images(test_recipes=False):
    # Check already existing file names
    images_extracted = [name.replace('.jpg', '') for name in os.listdir(config.IMAGE_FOLDER_PATH)]
    print('{} images already exists in the folder'.format(len(images_extracted)))

    # Retrieve images urls in the recipes.json
    all_recipes = load_json_to_list()
    if test_recipes:
        all_recipes = test_recipes

    all_img_urls = {extract_filename(recipe['url']): recipe['picture_link']
                    for recipe in all_recipes if recipe['picture_link']}

    # Filter already extracted images
    # 1. Collect keys to remove
    keys_to_remove = [key for key in all_img_urls.keys() if key in images_extracted]

    # 2. Remove collected keys after the loop
    for key in keys_to_remove:
        del all_img_urls[key]
    print(f'{len(all_img_urls)} images to be extracted.')

    # 3. Save images locally for filtered out image links
    for i, key in enumerate(all_img_urls.keys()):
        img_url = all_img_urls[key]
        save_image_locally(key, img_url)
        print(f'{i}: {img_url} saved.')

    # Update recipes and save them
    updated_recipes = update_recipes(all_recipes)
    save_to_json(updated_recipes, 'recipes_images.json')


if __name__ == '__main__':
    save_all_images()
