from multiprocessing import Pool
from combat.channel_extracting import channel_urls
from combat.page_parsing import get_channel_list, get_item_info, channel_list, item_info


def get_all_links(channel):
    for i in range(1, 100):
        get_channel_list(channel, i)


if __name__ == '__main__':
    pool = Pool(processes=20)
    # pool.map(get_all_links, channel_urls.split())
    db_urls = [item['item_url'] for item in channel_list.find()]
    index_urls = [item['item_url'] for item in item_info.find()]
    x = set(db_urls)
    y = set(index_urls)
    rest_of_urls = x - y
    print(rest_of_urls)
    pool.map(get_item_info, rest_of_urls)

