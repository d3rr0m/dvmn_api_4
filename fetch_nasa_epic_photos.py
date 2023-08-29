from datetime import date
import requests
from os import environ

from download_save_functions import download_save_image


def fetch_nasa_epic_photos(image_date, epic_count):
    url = 'https://api.nasa.gov/EPIC/api/natural/date/{date}'
    params = {
        'api_key': environ['NASA_API_TOKEN'],
    }
    response = requests.get(
        url=url.format(date=image_date),
        params=params,
        )
    response.raise_for_status()
    for i in range(epic_count):
        image_name = response.json()[i]['image']
        image_url = f'https://epic.gsfc.nasa.gov/archive/natural/'\
            f'{image_date.year}/{image_date.month:02d}/{image_date.day:02d}/'\
            f'png/{image_name}.png'
        download_save_image(image_url, f'images/{image_date}_{image_name}.png')


def get_nasa_epic_available_date():
    url = 'https://api.nasa.gov/EPIC/api/natural/all'
    params = {
        'api_key': environ['NASA_API_TOKEN'],
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    available_date = date.fromisoformat(response.json()[0]['date'])
    return available_date


if __name__ == '__main__':
    epic_available_date = get_nasa_epic_available_date()
    fetch_nasa_epic_photos(epic_available_date, 5)
