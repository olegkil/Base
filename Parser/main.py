import requests
from bs4 import BeautifulSoup
import time
from random import randrange
import json

headers = {
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36'
}

def get_song(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')
    pagination_count = int(soup.find('ul', class_='listalka').find_all('li')[-1].text)

    for page in range(1, pagination_count + 1):
    # for page in range(6, 10):
        response = s.get(url=f'https://ru-music.com/page/{page}/', headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        tracks_list = []

        for songs in {page}:
            songs = soup.find_all('li', class_="track")

            for data in songs:
                try:
                    track = data.find('div', class_='cover_image').find('img').get('title')
                except:
                    track = "Косяк на сайте"
                try:
                    artist = data.find('h2', class_='playlist-name').find('b').text
                except:
                    artist = "Косяк на сайте"
                try:
                    song = data.find('h2', class_='playlist-name').find('em').find('a').text
                except:
                    song = "Косяк на сайте"
                try:
                    download_url = "https://dl6.ru-music.cc/mp3/" + data.get('data-id')
                except:
                    download_url = "Косяк на сайте"


                tracks_list.append(
                    {
                    "Track" : track,
                    "Artist" : artist,
                    "Song" : song,
                    "URL download" : download_url
                    }
                )

        time.sleep(randrange(2, 5))
        print(f'Обработал {page}/{pagination_count}')

        with open('tracks_list.json', 'a') as file:
            # for text in tracks_list:
            #     file.write(f'{tracks_list}\n')
            json.dump(tracks_list, file, indent=4, ensure_ascii=False)

    return 'Работа по сбору данных завершина'

def main():
    print(get_song(url='https://ru-music.com/'))

if __name__ == '__main__':
    main()