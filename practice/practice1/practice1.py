# coding: utf-8


from bs4 import BeautifulSoup
import requests
import time
import pymongo
listing = []


page_url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'
headers = {
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
}
client = pymongo.MongoClient('localhost', 27017)
xiaozhu = client['xiaozhu']
sheet_listing = xiaozhu['sheet_listing']


def get_page_url(page):
    return page_url.format(str(page))


def get_listing(url, data=None):
    web_data = requests.get(url, headers=headers)
    time.sleep(1)
    soup = BeautifulSoup(web_data.text, 'lxml')
    urls = soup.select('ul > li > a.resule_img_a')
    imgs = soup.select('ul > li > a > img')
    prices = soup.select('div.result_btm_con.lodgeunitname > div > span > i')
    descriptions = soup.select('ul > li > div.result_btm_con.lodgeunitname > div.result_intro > em')
    comments = soup.select('div.result_btm_con.lodgeunitname > div.result_intro > em > span')
    for url, img, price, description, comment in zip(urls, imgs, prices, descriptions, comments):
        data = {
            'url': url.get('href'),
            'img': img.get('src'),
            'title': img.get('title'),
            'price': int(price.get_text()),
            'description': description.get_text(),
            'comment': comment.get_text()
        }
        print('Get info of', data['title'])
        listing.append(data)
        sheet_listing.insert_one(data)
    return listing


# for i in range(1, 3):
#     get_listing(get_page_url(i))


for item in sheet_listing.find({'price': {'$lt': 1000}}):
    if item['price'] >= 500:
        print(item['price'])


