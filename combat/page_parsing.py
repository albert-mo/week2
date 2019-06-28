from bs4 import BeautifulSoup
import requests
import time
import pymongo


client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
channel_list = ganji['channel_list']
item_info = ganji['item_info']


# 商家输入参数：'a2' 个人输入参数''
# http://bj.ganji.com/rirongbaihuo/o1/
# http://bj.ganji.com/rirongbaihuo/a2o2/
def get_channel_list(channel, page, business_type=''):
    url = (channel + '{}o{}/').format(business_type, str(page))
    web_data = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(web_data.text, 'lxml')
    titles = soup.select('dl.list-bigpic > dt > a')
    not_exist = len(soup.find_all('dl', 'list-bigpic')) == 0
    if not_exist:
        pass
    else:
        for title in titles:
            data = {
                'title': title.get('title'),
                'item_url': title.get('href')
            }
            channel_list.insert_one(data)
            print(data)


def get_item_info(item_url):
    web_data = requests.get(item_url)
    time.sleep(1)
    soup = BeautifulSoup(web_data.text, 'lxml')
    not_exist = len(soup.find_all('h1')) == 0
    if not_exist:
        pass
    else:
        title = soup.select_one('div.title-box h1')
        post_time = " ".join(soup.select_one('ul.title-info-l i.pr-5').get_text().split())
        type = soup.select_one('ul.det-infor > li:nth-child(1) > span >a')
        price = soup.select_one('ul > li:nth-child(2) > i.f22')
        area = "".join(soup.select_one('div:nth-child(2) > div > ul > li:nth-child(3)').text.split())
        print(item_url)
        data = {
            'title': title.get_text(),
            'item_url': item_url,
            'post_time': post_time,
            'type': type.get_text() if type is not None else None,
            'price': int(price.get_text()) if price is not None else None,
            'area': area
        }
        item_info.insert_one(data)
        print(data)


# get_channel_list('http://bj.ganji.com/jiaju/', 2, 'a2')
# get_item_info('http://bj.ganji.com/rirongbaihuo/3707192147x.htm')
