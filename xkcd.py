import random
import requests

def _get_comic_number():
    return random.randrange(1, 1000)

def get_xkcd_comic():
    url = f'https://xkcd.com/{_get_comic_number()}/info.0.json'
    print(url)
    r = requests.get(url)
    return r.text 
