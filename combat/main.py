from multiprocessing import Pool
from combat.page_parsing import get_channel_lists, get_channel_data, get_item_info_data, get_item_info, get_item_sold, get_all_item_urls

if __name__ == '__main__':
    pool = Pool(processes=20)
    # channel_data = get_channel_data()
    # pool.starmap(get_channel_lists, channel_data)
    # item_info_data = get_item_info_data()
    # pool.starmap(get_item_info, item_info_data)
    item_urls = get_all_item_urls()
    pool.map(get_item_sold, item_urls)
    pool.close()
    pool.join()
