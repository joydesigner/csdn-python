import os
import time
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

download_path = './crawler'

if not os.path.exists(download_path):
    os.makedirs(download_path)


def download_pic(url):
    ua = UserAgent()
    headers = {'User-Agent': ua.chrome}
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.text, 'lxml')
    content = soup.find('div', class_='article')  # get div wrapper
    images = content.find_all('img')  # get all movie img tag
    pic_link_list = [image['src'] for image in images]  # all img link
    pic_name_list = [image['alt'] for image in images]  # movie name
    for name, link in zip(pic_name_list, pic_link_list):
        urlretrieve(link, f'{download_path}/{name}.jpg')  # download
    print(f'{url} all movies pics download done!')


def main():
    start_urls = ['https://movie.douban.com/top250']
    for i in range(1, 10):
        start_urls.append(
            f'https://movie.douban.com/top250?start={25*i}&filter=')
    start_time = time.time()
    # for url in start_urls:
    #     download_pic(url)

    # with threads
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for url in start_urls:
            future = executor.submit(download_pic, url)
            futures.append(future)
    # wait till all threads are completed
    wait(futures, return_when=ALL_COMPLETED)
    # print(start_urls)
    end_time = time.time()

    print('=' * 50)
    print(f'run time: {end_time - start_time}')


if __name__ == '__main__':
    main()
