import argparse
import requests

from download_save_functions import download_save_image


def fetch_spacex_last_launch():
    parser = argparse.ArgumentParser(
        description='Программа скачивает и сохраняет на диск фото старта'\
             ' SpaceX. Можно передать в качестве агрумента ID запуска.'\
             'Если аргумент не указан будут загружены фото последнего старта.'
        )
    parser.add_argument('-launch_id', '--launch_id', default='latest', help='ID запуска SpaceX')
    args = parser.parse_args()

    spacex_api_url = f'https://api.spacexdata.com/v5/launches/{args.launch_id}'
    filename = 'images/spacex_{id}.jpg'
    response = requests.get(spacex_api_url)
    response.raise_for_status()
    pictures = response.json()['links']['flickr']['original']

    for idx, picture in enumerate(pictures):
        download_save_image(picture, filename.format(id=idx))


if __name__ == '__main__':
    fetch_spacex_last_launch()
