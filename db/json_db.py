import json
import os
import sys

# Add the `src` directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from src.config import *


def load_json_to_set(filename=RECIPES_URL_FILE_PATH):
    """Loads recipe links from a JSON file."""
    if os.path.exists(filename):
        with open(filename, "r") as f:
            loaded_json = set(json.load(f))
            print(f'{len(loaded_json)} recipes URLs exists in the file.')
            return loaded_json
    return set()


def load_json_to_list(filename=RECIPES_FILE_PATH):
    """Loads recipe links from a JSON file."""
    if os.path.exists(filename):
        with open(filename, "r") as f:
            loaded_json = json.load(f)
            print(f'{len(loaded_json)} recipes already scraped.')
            return loaded_json
    return []


def save_to_json(links, filename=RECIPES_URL_FILE_PATH):
    """Saves recipe links to a JSON file."""
    with open(filename, "w") as f:
        json.dump(list(links), f, indent=4)

