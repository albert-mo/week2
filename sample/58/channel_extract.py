# coding: utf-8
from bs4 import BeautifulSoup
import requests


start_url = 'https://bj.58.com/sale.shtml'
host_url = 'https://bj.58.com'


def get_channel_url(url):
    web_data = requests.get(start_url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    links = soup.select('ul.ym-submnu > li > b > a')
    for link in links:
        page_url = host_url + link.get('href')
        print(page_url)


# get_channel_url(start_url)
channel_list = '''
    https://bj.58.com/shouji/
    https://bj.58.com/tongxunyw/
    https://bj.58.com/danche/
    https://bj.58.com/diandongche/
    https://bj.58.com/fzixingche/
    https://bj.58.com/sanlunche/
    https://bj.58.com/peijianzhuangbei/
    https://bj.58.com/diannao/
    https://bj.58.com/bijiben/
    https://bj.58.com/pbdn/
    https://bj.58.com/diannaopeijian/
    https://bj.58.com/zhoubianshebei/
    https://bj.58.com/shuma/
    https://bj.58.com/shumaxiangji/
    https://bj.58.com/mpsanmpsi/
    https://bj.58.com/youxiji/
    https://bj.58.com/ershoukongtiao/
    https://bj.58.com/dianshiji/
    https://bj.58.com/xiyiji/
    https://bj.58.com/bingxiang/
    https://bj.58.com/jiadian/
    https://bj.58.com/binggui/
    https://bj.58.com/chuang/
    https://bj.58.com/ershoujiaju/
    https://bj.58.com/yingyou/
    https://bj.58.com/yingeryongpin/
    https://bj.58.com/muyingweiyang/
    https://bj.58.com/muyingtongchuang/
    https://bj.58.com/yunfuyongpin/
    https://bj.58.com/fushi/
    https://bj.58.com/nanzhuang/
    https://bj.58.com/fsxiemao/
    https://bj.58.com/xiangbao/
    https://bj.58.com/meirong/
    https://bj.58.com/yishu/
    https://bj.58.com/shufahuihua/
    https://bj.58.com/zhubaoshipin/
    https://bj.58.com/yuqi/
    https://bj.58.com/tushu/
    https://bj.58.com/tushubook/
    https://bj.58.com/wenti/
    https://bj.58.com/yundongfushi/
    https://bj.58.com/jianshenqixie/
    https://bj.58.com/huju/
    https://bj.58.com/qiulei/
    https://bj.58.com/yueqi/
    https://bj.58.com/kaquan/
    https://bj.58.com/bangongshebei/
    https://bj.58.com/diannaohaocai/
    https://bj.58.com/bangongjiaju/
    https://bj.58.com/ershoushebei/
    https://bj.58.com/chengren/
    https://bj.58.com/nvyongpin/
    https://bj.58.com/qinglvqingqu/
    https://bj.58.com/qingquneiyi/
    https://bj.58.com/chengren/
    https://bj.58.com/xiaoyuan/
    https://bj.58.com/ershouqiugou/
    https://bj.58.com/tiaozao/
    https://bj.58.com/tiaozao/
    https://bj.58.com/tiaozao/
'''