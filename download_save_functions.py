from os import path
from pathlib import Path
from urllib.parse import unquote, urlparse

import requests


def get_file_extension(url):
    print(url)
    url = unquote(url)
    file_path = urlparse(url).path
    filename = path.split(file_path)[1]
    extension = path.splitext(filename)[1]
    return extension


def download_save_image(url, path):
    response = requests.get(url)
    response.raise_for_status()
    Path('images').mkdir(parents=True, exist_ok=True)

    with open(path, 'wb') as file:
        file.write(response.content)
