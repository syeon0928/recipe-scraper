## Recipe scrapers (Personal Fork)

[![Build Status](https://travis-ci.org/hhursev/recipe-scraper.svg?branch=master)](https://travis-ci.org/hhursev/recipe-scraper)
[![Coverage Status](https://coveralls.io/repos/hhursev/recipe-scraper/badge.svg?branch=master&service=github)](https://coveralls.io/github/hhursev/recipe-scraper?branch=master)

**Note:** This is a personal fork of the original [recipe-scraper repository](https://github.com/hhursev/recipe-scraper) by [hhursev](https://github.com/hhursev) mainly modified for Epicurious website.

A web scraping tool for gathering structured recipe data from Epicurious.com as of 7th Nov 2024. This project is tailored for data analytics and data science, making it easy to collect, process, and store recipes for further analysis in recipe-related projects. Currently, only [Epicurious.com](epicurious.com) is fully supported with up-to-date scraping logic, though the code structure allows for future expansion to other recipe sites.

Find the dataset [here](https://www.kaggle.com/datasets/seungyeonhan1/recipe-dataset-with-images-tags-and-ratings/data)

### Modified Features in this Fork
1. Fix existing scraping code for recipe title, ingredients, instructions, image link and total time to match the changes in epicurious.com. 
2. Collected extra features such as recipe tags, description, ratings, rating counts, servings, author and publish date
3. Gathers all available recipe URLs from Epicurious, storing them in a JSON file for systematic scraping.
4. Saves scraped recipes for all possible recipes url to MongoDB or as a local JSON file, with images saved locally in an images folder.

### Usage
Clone the repository and install dependencies
```
git clone https://github.com/syeon0928/recipe-scraper.git
cd recipe-scraper
pip install -e .
```

Running main.py will first gather recipe list from epicurious.com, then save the individual recipes for all urls, and save the images as local file in 'db/images' directory.
```
python main.py
```
You can choose to save data in MongoDB. Set the MongoDB URI in the .env file if you want to use MongoDB as a storage backend.

```
python main.py --mongodb 
```




### Project Structure
```
recipe-scraper/
├── db/
│   ├── mongo_db.py          # MongoDB connection functions
│   ├── save_json.py         # JSON save functions
│   ├── save_images.py       # Logic to save images locally
│   ├── images/              # Directory for saving images locally
│   ├── recipe_urls.json     # JSON file storing all gathered recipe URLs
│   └── recipe.json          # JSON file storing all scraped recipe data
├── recipe_scrapers/
│   ├── _abstract.py         # Abstract class for scraper classes
│   ├── _util.py             # Helper functions
│   ├── epicurious.py        # Scraping Epicurious.com recipe
│   └── etc.                 # More scrapers (NEED TO BE UPDATED)
├── src/
│   ├── gather_urls.py       # Logic to gather recipe URLs from Epicurious.com
│   ├── scrape.py            # Logic to scrape each recipe URL using recipe-scraper
│   └── util.py              # Helper functions
├── config.py                # Configuration file for MongoDB and other settings
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
├── test.py                  # Running all tests
└── main.py                  # Main script for running the entire scraping process
```
### TODO
Extend the logic to other websites.

---
### Original ReadMe
A simple web scraping tool for recipe sites I use in a project of mine that makes sense to live as
a separate package. **No Python 2 support.**

    pip install git+git://github.com/hhursev/recipe-scraper.git

then:

    from recipe_scrapers import scrap_me

    # give the url as a string, it can be url from any site listed below
    scrap_me = scrap_me('http://allrecipes.com/Recipe/Apple-Cake-Iv/Detail.aspx')

    scrap_me.title()
    scrap_me.total_time()
    scrap_me.ingredients()
    scrap_me.instructions()


### Contribute

Part of the reason I want this open sourced is because if a site makes a design change, the scraper
for it should be modified.

If you spot a design change (or something else) that makes the scrapers unable to work for the given
site - please fire an issue asap.

If you are programmer PRs with fixes are warmly welcomed and acknowledged with a virtual beer
 :beer:.


### Scrapers available for:

- [http://101cookbooks.com/](http://101cookbooks.com/)
- [http://allrecipes.com/](http://allrecipes.com/)
- [http://bbc.co.uk/](http://bbc.co.uk/food/recipes/)
- [http://bbcgoodfood.com/](http://bbcgoodfood.com/)
- [http://bonappetit.com/](http://bonappetit.com/)
- [http://closetcooking.com/](http://closetcooking.com/)
- [http://cookstr.com/](http://cookstr.com/)
- [http://epicurious.com/](http://epicurious.com/) (**Updated**)
- [http://finedininglovers.com/](https://www.finedininglovers.com/)
- [http://foodrepublic.com/](http://foodrepublic.com)
- [http://jamieoliver.com/](http://www.jamieoliver.com/)
- [http://mybakingaddiction.com/](http://mybakingaddiction.com/)
- [http://paninihappy.com/](http://paninihappy.com/)
- [http://realsimple.com/](http://www.realsimple.com/)
- [http://simplyrecipes.com/](http://www.simplyrecipes.com)
- [http://steamykitchen.com/](http://steamykitchen.com/)
- [http://tastykitchen.com/](http://tastykitchen.com/)
- [http://thepioneerwoman.com/](http://thepioneerwoman.com/)
- [http://thevintagemixer.com/](http://www.thevintagemixer.com/)
- [http://twopeasandtheirpod.com/](http://twopeasandtheirpod.com/)
- [http://whatsgabycooking.com/](http://whatsgabycooking.com/)
