from bs4 import BeautifulSoup
import requests
from combat.mongo_db import insert_category


start_url = 'http://bj.ganji.com/wu/'
base_url = 'http://bj.ganji.com'


def extract_urls(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    urls = soup.select('div.content dt > a')
    for url in urls:
        data = {
            'sort': url.get_text(),
            'url': base_url + url.get('href')
        }
        insert_category(data)
        print(data)


extract_urls(start_url)
