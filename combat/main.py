from multiprocessing import Pool
from combat.page_parsing import get_channel_lists, get_channel_data, get_item_info_data, get_item_info

if __name__ == '__main__':
    pool = Pool(processes=20)
    # channel_data = get_channel_data()
    # pool.starmap(get_channel_lists, channel_data)
    item_info_data = get_item_info_data()
    pool.starmap(get_item_info, item_info_data)
    pool.close()
    pool.join()
