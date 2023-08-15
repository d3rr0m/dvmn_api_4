import requests
from pathlib import Path


def download_save_image(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)

def main():
    filename = 'images/hubble.jpeg'
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    download_save_image(url, filename)

    Path('images').mkdir(parents=True, exist_ok=True)
    

if __name__ == '__main__':
    main()
