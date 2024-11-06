import os
import requests
from pymongo import MongoClient
from pymongo.server_api import ServerApi

MONGO_URI = os.getenv('MONGO_URI')

client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
client.server_info()
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client["recipes_db"]
collection = db["recipes"]


def insert_recipe(recipe_data):
    """Insert a recipe into the MongoDB collection."""
    if recipe_data:
        # Upsert: Insert or update by URL to avoid duplicates
        collection.update_one({'url': recipe_data['url']}, {"$set": recipe_data}, upsert=True)
        print(f"Recipe for {recipe_data['url']} saved to MongoDB.")

