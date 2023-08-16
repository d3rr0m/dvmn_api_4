import requests
import pprint
from pathlib import Path


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
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
