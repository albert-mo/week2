import time
from combat.page_parsing import item_info


while True:
    print(item_info.find().count())
    time.sleep(5)
