# coding: utf-8
from bs4 import BeautifulSoup
import requests


start_url = 'https://bj.tongcheng.com/sale.shtml'
host_url = 'https://bj.tongcheng.com'


def get_channel_url(url):
    web_data = requests.get(start_url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    links = soup.select('ul.ym-submnu > li > b > a')
    for link in links:
        page_url = host_url + link.get('href')
        print(page_url)


get_channel_url(start_url)
channel_list = '''
    https://bj.tongcheng.com/shouji/
    https://bj.tongcheng.com/tongxunyw/
    https://bj.tongcheng.com/danche/
    https://bj.tongcheng.com/diandongche/
    https://bj.tongcheng.com/fzixingche/
    https://bj.tongcheng.com/sanlunche/
    https://bj.tongcheng.com/peijianzhuangbei/
    https://bj.tongcheng.com/diannao/
    https://bj.tongcheng.com/bijiben/
    https://bj.tongcheng.com/pbdn/
    https://bj.tongcheng.com/diannaopeijian/
    https://bj.tongcheng.com/zhoubianshebei/
    https://bj.tongcheng.com/shuma/
    https://bj.tongcheng.com/shumaxiangji/
    https://bj.tongcheng.com/mpsanmpsi/
    https://bj.tongcheng.com/youxiji/
    https://bj.tongcheng.com/ershoukongtiao/
    https://bj.tongcheng.com/dianshiji/
    https://bj.tongcheng.com/xiyiji/
    https://bj.tongcheng.com/bingxiang/
    https://bj.tongcheng.com/jiadian/
    https://bj.tongcheng.com/binggui/
    https://bj.tongcheng.com/chuang/
    https://bj.tongcheng.com/ershoujiaju/
    https://bj.tongcheng.com/yingyou/
    https://bj.tongcheng.com/yingeryongpin/
    https://bj.tongcheng.com/muyingweiyang/
    https://bj.tongcheng.com/muyingtongchuang/
    https://bj.tongcheng.com/yunfuyongpin/
    https://bj.tongcheng.com/fushi/
    https://bj.tongcheng.com/nanzhuang/
    https://bj.tongcheng.com/fsxiemao/
    https://bj.tongcheng.com/xiangbao/
    https://bj.tongcheng.com/meirong/
    https://bj.tongcheng.com/yishu/
    https://bj.tongcheng.com/shufahuihua/
    https://bj.tongcheng.com/zhubaoshipin/
    https://bj.tongcheng.com/yuqi/
    https://bj.tongcheng.com/tushu/
    https://bj.tongcheng.com/tushubook/
    https://bj.tongcheng.com/wenti/
    https://bj.tongcheng.com/yundongfushi/
    https://bj.tongcheng.com/jianshenqixie/
    https://bj.tongcheng.com/huju/
    https://bj.tongcheng.com/qiulei/
    https://bj.tongcheng.com/yueqi/
    https://bj.tongcheng.com/kaquan/
    https://bj.tongcheng.com/bangongshebei/
    https://bj.tongcheng.com/diannaohaocai/
    https://bj.tongcheng.com/bangongjiaju/
    https://bj.tongcheng.com/ershoushebei/
    https://bj.tongcheng.com/chengren/
    https://bj.tongcheng.com/nvyongpin/
    https://bj.tongcheng.com/qinglvqingqu/
    https://bj.tongcheng.com/qingquneiyi/
    https://bj.tongcheng.com/chengren/
    https://bj.tongcheng.com/xiaoyuan/
    https://bj.tongcheng.com/ershouqiugou/
    https://bj.tongcheng.com/tiaozao/
    https://bj.tongcheng.com/tiaozao/
    https://bj.tongcheng.com/tiaozao/
'''