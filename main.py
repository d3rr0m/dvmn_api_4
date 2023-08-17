import requests
from pathlib import Path
from dotenv import dotenv_values
import pprint
from urllib.parse import urlparse, unquote
from os import path


config = dotenv_values('.env')


SPACEX_FLIGHT_ID = '5eb87ce3ffd86e000604b336'
SPACEX_API_URL = 'https://api.spacexdata.com/v5/launches/{id}'


def fetch_spacex_last_launch():
    filename = 'images/spacex_{id}.jpg'
    response = requests.get(SPACEX_API_URL.format(id=SPACEX_FLIGHT_ID))
    response.raise_for_status()
    pictures = response.json()['links']['flickr']['original']
    Path('images').mkdir(parents=True, exist_ok=True)

    for idx, picture in enumerate(pictures):
        download_save_image(picture, filename.format(id=idx))


def download_save_image(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)

def main():
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': config['NASA_API_TOKEN'],
        'date': '2023-08-14'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    url = unquote(response.json()['url'])
    file_path = urlparse(url).path
    _, filename = path.split(file_path)
    print (filename)
    response = requests.get(url)
    response.raise_for_status()
    with open ('nasa.jpg', 'wb') as file:
        file.write(response.content)
    #download_save_image()
    #fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
