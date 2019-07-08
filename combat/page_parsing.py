from string import punctuation

from bs4 import BeautifulSoup
import requests
import time
import random
from combat.mongo_db import channel_list, category, item_info, insert_item, update_item_time


def get_channel_lists(channel, sort):
    for item in range(1, 11):
        get_channel_list(channel, item, sort)


def get_channel_data():
    channels = [item['url'] for item in category.find()]
    sorts = [item['sort'] for item in category.find()]
    print(channels)
    print(sorts)
    return zip(channels, sorts)


# 商家输入参数：'a2' 个人输入参数'a1'
# http://bj.ganji.com/rirongbaihuo/a1o1/
# http://bj.ganji.com/rirongbaihuo/a2o2/
def get_channel_list(channel, page, sort, business_type='a1'):
    url = (channel + '{}o{}/').format(business_type, str(page))
    web_data = requests.get(url)
    time.sleep(random.random() * 3)
    soup = BeautifulSoup(web_data.text, 'lxml')
    titles = soup.select('dl.list-bigpic > dt > a')
    # not_exist = len(soup.find_all('dl', 'list-bigpic')) == 0
    # if not_exist:
    if soup.find_all('dl', 'list-bigpic'):
        for title in titles:
            data = {
                'title': title.get('title'),
                'item_url': title.get('href'),
                'sort': sort
            }
            insert_item(channel_list, data, 'item_url')
            print(data)
    else:
        print('Page {} out of range'.format(page))


def get_item_info_data():
    db_urls = [item['item_url'] for item in channel_list.find()]
    index_urls = [item['item_url'] for item in item_info.find()]
    x = set(db_urls)
    y = set(index_urls)
    rest_of_urls = x - y
    sorts = []
    for item in rest_of_urls:
        sort = channel_list.find_one({'item_url': item})
        sorts.append(sort['sort'])
    print(len(rest_of_urls), ':', rest_of_urls)
    print(sorts, ':', len(sorts))
    return zip(rest_of_urls, sorts)


def get_all_item_urls():
    index_urls = [item['item_url'] for item in item_info.find()]
    print(len(index_urls), ':', index_urls)
    return index_urls


def get_item_info(item_url, sort):
    web_data = requests.get(item_url)
    time.sleep(random.random() * 3)
    soup = BeautifulSoup(web_data.text, 'lxml')
    if soup.find_all('h1'):
        title = soup.select_one('div.title-box h1')
        post_time = " ".join(soup.select_one('ul.title-info-l i.pr-5').get_text().split())
        type = soup.select_one('ul.det-infor > li:nth-child(1) > span >a')
        price = soup.select_one('ul > li:nth-child(2) > i.f22')
        area = list(soup.select_one('div:nth-child(2) > div > ul > li:nth-child(3)').stripped_strings)
        area = [i for i in area if i not in punctuation]
        del area[0]
        data = {
            'title': title.get_text(),
            'item_url': item_url,
            'post_time': post_time,
            'type': type.get_text() if type is not None else None,
            'price': int(price.get_text()) if price is not None else None,
            'area': area,
            'sort': sort
        }
        insert_item(item_info, data, 'item_url')
        print(data)
    else:
        update_item_time(item_info, item_url)
        print('商品已售出')


def get_item_sold(item_url):
    try:
        web_data = requests.get(item_url)
        time.sleep(random.random() * 3)
        soup = BeautifulSoup(web_data.text, 'lxml')
        if soup.find_all('h1'):
            pass
        else:
            update_item_time(item_info, item_url)
            print('商品已售出')
    except:
        print('except')


# get_channel_list('http://bj.ganji.com/jiaju/', 2, '二手家具', 'a2')
# get_item_info('http://bj.ganji.com/rirongbaihuo/3628142725x.htm', '窗帘')
# print(get_channel_data())
# print(get_item_info_data())
