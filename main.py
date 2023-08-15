import requests
from pathlib import Path


def main():
    filename = 'images/hubble.jpeg'
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    response = requests.get(url)
    response.raise_for_status()

    Path('images').mkdir(parents=True, exist_ok=True)
    with open(filename, 'wb') as file:
        file.write(response.content)

if __name__ == '__main__':
    main()
