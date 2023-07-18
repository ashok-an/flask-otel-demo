import random
import requests

import pymongo
from opentelemetry.instrumentation.pymongo import PymongoInstrumentor

PymongoInstrumentor().instrument()
db_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = db_client['comics'] 
collection = db['xkcd']


def get_xkcd_comic_from_db(number):
    return collection.find_one({'_id': number})


def add_xkcd_comic_to_db(data):
    data['_id'] = data.get('num', 0)
    collection.insert_one(data)


def get_xkcd_comic_from_url(number):
    url = f'https://xkcd.com/{number}/info.0.json'
    print(url)
    r = requests.get(url)
    output = r.json()
    add_xkcd_comic_to_db(output)
    return output


def _get_comic_number():
    return random.randrange(1, 20)


def get_xkcd_comic():
    number = _get_comic_number()
    db_data = get_xkcd_comic_from_db(number)
    if db_data:
        return db_data
    else:
        return get_xkcd_comic_from_url(number)
