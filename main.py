import requests
from pathlib import Path
from dotenv import dotenv_values
import pprint
from urllib.parse import urlparse, unquote
from os import path
from datetime import date, timedelta


config = dotenv_values('.env')






def fetch_spacex_last_launch():
    spacex_api_url = 'https://api.spacexdata.com/v5/launches/{id}'
    spacex_flight_id = '5eb87ce3ffd86e000604b336'
    filename = 'images/spacex_{id}.jpg'
    response = requests.get(spacex_api_url.format(id=spacex_flight_id))
    response.raise_for_status()
    pictures = response.json()['links']['flickr']['original']
    

    for idx, picture in enumerate(pictures):
        download_save_image(picture, filename.format(id=idx))


def download_save_image(url, path):
    response = requests.get(url)
    response.raise_for_status()
    Path('images').mkdir(parents=True, exist_ok=True)
    
    with open(path, 'wb') as file:
        file.write(response.content)


def get_file_extension(filename):
    extension = path.splitext(filename)[1]
    return extension


def fetch_nasa_apod():
    url = 'https://api.nasa.gov/planetary/apod'
    yeasterday_date = str(date.today()-timedelta(days=1))
    params = {
        'api_key': config['NASA_API_TOKEN'],
        'date': yeasterday_date
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    url = unquote(response.json()['url'])
    file_path = urlparse(url).path
    filename = path.split(file_path)[1]
    extension = get_file_extension(filename)
    response = requests.get(url)
    response.raise_for_status()
    with open (f'nasa_apod_{yeasterday_date}{extension}', 'wb') as file:
        file.write(response.content)


def main():
    fetch_nasa_apod()
    
    #download_save_image()
    #fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
