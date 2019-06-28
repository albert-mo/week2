import time
from sample.tongcheng.pages_parsing import url_list

while True:
    print(url_list.find().count())
    time.sleep(5)
