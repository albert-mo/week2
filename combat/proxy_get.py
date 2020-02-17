import telnetlib

from bs4 import BeautifulSoup
import requests, time, random
from multiprocessing import Pool
from combat.mongo_db import insert_proxy, update_proxy, xici, reset_proxy, get_valid_proxy

xici_url = 'https://www.xicidaili.com/wn/{}'
qydaili_url = 'http://www.qydaili.com/free/?action=china&page={}'
ihuan_url = 'https://ip.ihuan.me/ti.html'
eight_urls = 'http://www.89ip.cn/tqdl.html?api=1&num={}&port=&address=&isp='
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36
# proxies = {'http': 'http://{}:{}'.format('120.83.109.39', '9999')}
'''
    通过读取数据库获取随机proxies
'''


def get_valid_proxies():
    proxy_list = get_valid_proxy()
    # 随机获取代理ip
    print('proxies nubmer:{}'.format(len(proxy_list)))
    proxy_ip = random.choice(proxy_list)
    proxies = {'https': proxy_ip}
    return proxies


def get_proxy_xici(page):
    print('Get info from page {}'.format(str(page)))
    web_data = requests.get(xici_url.format(str(page)), headers=headers)
    time.sleep(random.random() * 3)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.select('tr.odd td:nth-child(2)')
    ports = soup.select('tr.odd td:nth-child(3)')
    addrs = soup.select('tr.odd td:nth-child(4)')
    anonymouss = soup.select('tr.odd td:nth-child(5)')
    speeds = soup.select('tr.odd td:nth-child(7) div div')
    # print(ips)
    for ip, port, addr, anonymous, speed in zip(ips, ports, addrs, anonymouss, speeds):
        data = {
            'ip': ip.get_text(),
            'port': port.get_text(),
            'addr': addr.get_text(),
            'anonymous': anonymous.get_text(),
            'speed': speed.get('style'),
            'status': 'unknown',
            'type': 'https'
        }
        insert_proxy(data)
        print(data)


def get_proxy_qydaili(page):
    print('Get info from {}'.format(qydaili_url.format(str(page))))
    web_data = requests.get(qydaili_url.format(str(page)), headers=headers)
    time.sleep(random.random() * 3)
    soup = BeautifulSoup(web_data.text, 'lxml')
    # print(soup)
    ips = soup.select('tbody tr td:nth-child(1)')
    ports = soup.select('tbody tr td:nth-child(2)')
    addrs = soup.select('tbody tr td:nth-child(5)')
    anonymouss = soup.select('tbody tr td:nth-child(3)')
    types = soup.select('tbody tr td:nth-child(4)')
    for ip, port, addr, anonymous, type in zip(ips, ports, addrs, anonymouss, types):
        data = {
            'ip': ip.get_text(),
            'port': port.get_text(),
            'addr': addr.get_text(),
            'anonymous': anonymous.get_text(),
            'speed': 'none',
            'status': 'unknown',
            'type': type.get_text()
        }
        insert_proxy(data)
        print(data)


def get_proxy_89(num):
    print('Get info from {}'.format(eight_urls.format(str(num))))
    web_data = requests.get(eight_urls.format(str(num)), headers=headers)
    time.sleep(random.random() * 3)
    soup = BeautifulSoup(web_data.text, 'lxml')
    res = str(soup).split()[-1].split('<br/>')
    res.pop()
    res.remove('')
    print(res)
    for item in res:
        try:
            data = {
                'ip': item.split(':')[0],
                'port': item.split(':')[1],
                'addr': 'none',
                'anonymous': 'none',
                'speed': 'none',
                'status': 'unknown',
                'type': 'none'
            }
            insert_proxy(data)
            print(data)
        except:
            print('Error')
        else:
            pass


def test_status_requsets(data):
    try:
        requests.get('https://www.japonx.net', proxies={"https": "https://{}:{}".format(data['ip'], data['port'])})
    except:
        update_proxy(data['ip'], data['port'], 'fail')
        print('connect failed')
    else:
        update_proxy(data['ip'], data['port'], 'success')
        print('{}:success'.format(data['ip']))


def test_status_telnet(data):
    try:
        telnetlib.Telnet(data['ip'], port=data['port'], timeout=20)
    except:
        print('connect failed')
    else:
        print('{}:success'.format(data['ip']))


if __name__ == '__main__':
    pool = Pool(processes=50)
    whether_api = 0
    whether_get = 0
    whether_test = 1
    if whether_api == 1:
        get_proxy_89(3000)
    if whether_get == 1:
        pages = [i for i in range(1, 101)]
        pool.map(get_proxy_xici, pages)
    if whether_test == 1:
        # reset_proxy()
        datas = xici.find({'status': {'$ne': 'fail'}})
        print('test status of {} proxies'.format(datas.count()))
        pool.map(test_status_requsets, datas)
    pool.close()
    pool.join()
