import certifi
import ssl
from os import path
from urllib import request
import src.config as config
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


def main(test_recipes=False):
    # Check already existing file names
    images_extracted = set(os.listdir(config.IMAGE_FOLDER_PATH))
    print('{} images already exists in the folder'.format(len(images_extracted)))

    # Retrieve images urls in the recipes.json
    all_recipes = load_json_to_list()
    if test_recipes:
        all_recipes = test_recipes

    all_img_urls = {extract_filename(recipe['url']): recipe['picture_link']
                    for recipe in all_recipes if recipe['picture_link']}

    # Filter already extracted images
    for key in all_img_urls.keys():
        if key in images_extracted:
            del all_img_urls[key]
    print(f'{len(all_img_urls)} images to be extracted.')

    # Save images locally for filtered out image links
    for i, key in enumerate(all_img_urls.keys()):
        img_url = all_img_urls[key]
        save_image_locally(key, img_url)
        print(f'{i}: {img_url} saved.')


if __name__ == '__main__':
    main()
