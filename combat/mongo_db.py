import pymongo


client = pymongo.MongoClient('localhost', 27017)
proxy = client['proxy']
xici = proxy['xici']
ganji = client['ganji']
channel_list = ganji['channel_list']
item_info = ganji['item_info']
category = ganji['category']
item_info_back = ganji['item_info_back']


'''
    把t1复制到t2
'''


def backup(t1, t2):
    for item in t1.find():
        t2.insert_one(item)


'''
    保存代理资源
'''


def insert_proxy(data):
    if xici.find_one({'ip': data['ip'], 'port': data['port']}):
        print('Aleady exist')
    else:
        xici.insert_one(data)


'''
    更新代理资源
'''


def update_proxy(ip, port, status):
    xici.update({'ip': ip, 'port': port}, {'$set': {'status': status}})


'''
    重置代理状态
'''


def reset_proxy():
    for item in xici.find():
        xici.update({'ip': item['ip']}, {'$set': {'status': 'unknown'}})


'''
    获取所有有效代理
'''


def get_valid_proxy():
    res = xici.find({'status': 'success'})
    valid_proxy = ['https://{}:{}'.format(item['ip'], item['port']) for item in res]
    return valid_proxy


'''
    删除无效代理
'''


def del_invalid_proxy(ip):
    xici.remove({'ip': ip})


'''
    保存category
'''


def insert_category(data):
    if category.find_one({'sort': data['sort']}):
        print('Already exist')
    else:
        category.insert_one(data)


'''
    保存item
'''


def insert_item(table, data, item):
    print(item, '-', data[item])
    if table.find_one({item: data[item]}):
        print('Already exist')
    else:
        table.insert_one(data)


'''
    通过表名、url判断信息是否已经爬取
'''


def judge_info_got(table, url):
    if table.find_one({'item_url': url}):
        return True
    else:
        return False


'''
    删除表信息
'''


def del_table(table, condition):
    table.remove(condition)


# backup(item_info, item_info_back)


