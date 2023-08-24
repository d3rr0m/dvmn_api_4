from datetime import date, timedelta
import requests
from dotenv import load_dotenv
import os

from common_functions import download_save_image, get_file_extension


load_dotenv()


def fetch_nasa_apod_bulk(count):
    image_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': os.environ['NASA_API_TOKEN'],
        'count': count,
    }
    response = requests.get(image_url, params=params)
    response.raise_for_status()

    for idx, image_url in enumerate(response.json()):
        extension = get_file_extension(image_url['url'])
        download_save_image(image_url['url'], f'images/nasa_apod_{idx}{extension}')


def fetch_nasa_apod_today():
    url = 'https://api.nasa.gov/planetary/apod'
    yeasterday_date = str(date.today()-timedelta(days=1))
    params = {
        'api_key': os.environ['NASA_API_TOKEN'],
        'date': yeasterday_date,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    url = response.json()['url']
    extension = get_file_extension(url)
    download_save_image(url, f'images/nasa_apod_{yeasterday_date}{extension}')


if __name__ == '__main__':
    fetch_nasa_apod_today()