from common_functions import download_save_image


import requests


def fetch_spacex_last_launch():
    spacex_api_url = 'https://api.spacexdata.com/v5/launches/{flight_id}'
    spacex_flight_id = '5eb87ce3ffd86e000604b336'
    filename = 'images/spacex_{id}.jpg'
    response = requests.get(spacex_api_url.format(flight_id=spacex_flight_id))
    response.raise_for_status()
    pictures = response.json()['links']['flickr']['original']

    for idx, picture in enumerate(pictures):
        download_save_image(picture, filename.format(id=idx))


if __name__ == '__main__':
    fetch_spacex_last_launch()
