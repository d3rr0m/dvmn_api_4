from dotenv import load_dotenv
from urllib.parse import urlparse, unquote
from fetch_nasa_epic_photos import fetch_nasa_epic_photos, get_nasa_epic_available_date


load_dotenv()


def main():
    fetch_nasa_epic_photos(get_nasa_epic_available_date(), 5)
    #print(get_nasa_epic_available_date())
    #fetch_nasa_apod_bulk(5)
    #fetch_nasa_apod_today()
    #download_save_image()
    #fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
