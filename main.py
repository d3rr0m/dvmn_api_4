import requests
from dotenv import dotenv_values
import pprint
from datetime import date, timedelta

from common_functions import download_save_image, get_file_extension


config = dotenv_values('.env')


def get_nasa_epic_available_date():
    url = 'https://api.nasa.gov/EPIC/api/natural/all'
    params = {
        'api_key': config['NASA_API_TOKEN'],
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()[0]


def fetch_nasa_epic_photos(dates):
    url = 'https://api.nasa.gov/EPIC/api/natural/date/{date}'
    params = {
        'api_key': config['NASA_API_TOKEN'],
    }
    image_date = date.fromisoformat(dates['date'])
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


def fetch_nasa_apod_bulk(count):
    image_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': config['NASA_API_TOKEN'],
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
        'api_key': config['NASA_API_TOKEN'],
        'date': yeasterday_date,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    url = response.json()['url']
    extension = get_file_extension(url)
    download_save_image(url, f'images/nasa_apod_{yeasterday_date}{extension}')


def main():
    fetch_nasa_epic_photos(get_nasa_epic_available_date())
    print(get_nasa_epic_available_date())
    #fetch_nasa_apod_bulk(5)
    #fetch_nasa_apod_today()
    #download_save_image()
    #fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
