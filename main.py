import requests
from dotenv import load_dotenv
import pprint
import os
from urllib.parse import urlparse, unquote
import datetime
from common_functions import download_save_image


load_dotenv()


def get_nasa_epic_available_date():
    url = 'https://api.nasa.gov/EPIC/api/natural/all'
    params = {
        'api_key': os.environ['NASA_API_TOKEN'],
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()[0]


def fetch_nasa_epic_photos(date):
    url = 'https://api.nasa.gov/EPIC/api/natural/date/{date}'
    params = {
        'api_key': os.environ['NASA_API_TOKEN'],
    }
    image_date = datetime.date.fromisoformat(date['date'])
    response = requests.get(
        url=url.format(date=image_date),
        params=params,
        )
    response.raise_for_status()
    for i in range(10):
        image_name = response.json()[i]['image']
        image_url = f'https://epic.gsfc.nasa.gov/archive/natural/'\
            f'{image_date.year}/{image_date.month:02d}/{image_date.day:02d}/'\
            f'png/{image_name}.png'
        download_save_image(image_url, f'images/{image_date}_{image_name}.png')


def main():
    fetch_nasa_epic_photos(get_nasa_epic_available_date())
    #print(get_nasa_epic_available_date())
    #fetch_nasa_apod_bulk(5)
    #fetch_nasa_apod_today()
    #download_save_image()
    #fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
