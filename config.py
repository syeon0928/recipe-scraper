import os

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
}

BASE_URL = 'https://www.epicurious.com/'
RECIPE_URL = 'recipes/food/views/'

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))
RECIPES_URL_FILE_PATH = os.path.join(PROJECT_ROOT, 'db/recipe_urls.json')
RECIPES_FILE_PATH = os.path.join(PROJECT_ROOT, 'db/recipes.json')
IMAGE_FOLDER_PATH = os.path.join(PROJECT_ROOT, 'db/images')

recipe_menus = {

    'most_popular': 'recipes-menus/most-popular-recipes-gallery',
    'short_time': 'recipes-menus/30-minute-meals-gallery',
    'fe_ingredients': 'recipes-menus/5-ingredient-meals-gallery',
    'make_ahead': 'recipes-menus/make-ahead-weeknight-dinners-stew-soup-freezer-casserole-quick-easy-recipes-gallery',
    'one_pot': 'recipes-menus/our-favorite-one-pot-dinners-gallery',
    'breakfast': 'recipes-menus/best-breakfast-recipes-gallery',
    'dinner': 'recipes-menus/easy-dinner-ideas',
    'dessert': 'recipes-menus/71-easy-dessert-recipes-for-baking-beginners-and-tired-cooks-gallery',
    'drinks': 'recipes-menus/easy-cocktails-recipes-drinks-gallery',
    'chicken_grill': 'recipes-menus/grilled-chicken-recipes',
    'vegetable_grill': 'recipes-menus/grilled-vegetable-side-dish-recipes-gallery',
    'seafood_grill': 'recipes-menus/best-grilled-seafood-recipes-gallery',
    'cakes': 'recipes-menus/easy-cake-recipes-for-beginners-gallery',
    'slow_cooker': 'recipes-menus/crock-pot-slow-cooker-recipes',
    'vegetable_roast': 'recipes-menus/roasted-vegetables-gallery',
    'chicken_roast': 'recipes-menus/roast-chicken-variations-gallery',
    'bread': 'recipes-menus/the-best-bread-recipes-gallery',
    'cookies': 'recipes-menus/best-cookie-recipes-chocolate-chip-raisin-peanut-butter-gallery',
    'air_fryer': 'recipes-menus/air-fryer-recipes',
    'vegetarian': 'recipes-menus/our-favorite-vegetarian-recipes',
    'vegan': 'recipes-menus/vegan-recipes-gallery',
    'bon_appetit_2024': 'recipes-menus/bon-appetit-november-2024-issue',
    'aperol': 'recipes-menus/best-aperol-cocktails-gallery',
    'cocktails': 'recipes-menus/hidden-gem-cocktails',
    'gin_cocktails': 'recipes-menus/gin-cocktails',
    'chicken': 'ingredients/easy-chicken-dinner-recipes-gallery',
    'pork': 'recipes-menus/easy-pork-recipes-gallery',
    'grill_meat': 'recipes-menus/best-grilled-meat-recipes-gallery',
    'dinner_party': 'recipes-menus/elegant-one-bite-hors-d-oeuvres-gallery',
    'more_cocktails': 'recipes-menus/batch-cocktails',
    'birthday_cakes': 'recipes-menus/our-favorite-birthday-cakes-gallery',
    'lamb': 'recipes-menus/lamb-recipes-gallery',
    'salmon': 'ingredients/best-salmon-recipes-dinner-ideas-gallery',
    'shrimp': 'ingredients/shrimp-recipes-gallery',
    'burger': 'recipes-menus/best-burger-hamburger-recipes-memorial-day-barbecue-cookout-gallery',
    'cod': 'recipes-menus/cod-recipes',
    'tuna': 'ingredients/11-things-to-do-with-a-can-of-tuna-gallery',
    'scallop': 'recipes-menus/simple-scallop-recipes-gallery',
    'tofu': 'ingredients/tofu-recipes',
    'egg': 'recipes-menus/best-egg-recipes-gallery',
    'lentils': 'ingredients/best-lentil-recipes',
    'chickpea': 'ingredients/best-chickpea-recipes',
    'black_bean': 'recipes-menus/black-bean-recipes',
    'risotto': 'recipes-menus/risotto-many-ways-gallery',
    'noodle': 'recipes-menus/most-popular-noodles-and-pasta-recipes-2023',
    'tequila': 'ingredients/tequila-cocktails-beyond-margaritas-gallery',
    'vodka': 'recipes-menus/best-vodka-cocktails',
    'paneer': 'ingredients/best-paneer-recipes',
    'clams': 'recipes-menus/best-clam-recipes-gallery',
    'more_chicken': 'ingredients/easy-chicken-dinner-recipes-gallery',
    'mocktails': 'recipes-menus/nonalcoholic-drink-recipes',
    'fall_fest': 'recipes-menus/19-main-courses-for-a-fall-feast-gallery',
    'rosh_hashanah': 'recipes-menus/rosh-hashanah-recipes-to-celebrate-the-new-year-gallery',
    'holloween': 'holidays-events/easy-halloween-appetizers-and-snack-recipes-gallery',
    'thanksgiving': 'holidays-events/easiest-thanksgiving-recipes-gallery',

}

recipe_lists = ['ingredient/broccoli', 'ingredient/shrimp', 'ingredient/beets', 'ingredient/cauliflower',
                'ingredient/beef', 'type/lunch', 'ingredient/rice', 'ingredient/cod', 'ingredient/tofu',
                'ingredient/quinoa', 'ingredient/polenta', 'ingredient/whiskey', 'type/cocktail',
                'simple-cooking/weeknight-meals', 'ingredient/chickpea', 'ingredient/apple',
                'ingredient/cranberry', 'ingredient/fig', 'ingredient/pear']
