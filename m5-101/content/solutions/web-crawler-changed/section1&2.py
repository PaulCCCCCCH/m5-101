from posix import listdir
import requests
from bs4 import BeautifulSoup as bs
import math
import sys, getopt
import re
import os

def re_cleaner(target: str, rep: str) -> str:
    return re.sub("[^0-9a-zA-Z]+", rep, target)

def download_pages_oxford():
    ########################
    ### Section 1 Starts ###

    base_url = "" # 初始网页
    base_dir = "" # 要把页面保存在哪个文件夹

    base_page = requests.get(base_url)  # 拉取主页
    bs4 = BeautifulSoup(base_page.text)      # 把主页变成 BeautifulSoup 对象

    course_divs = None                 # 获取主页上所有项目链接
    for div in course_divs:
        # 从 div 中解析url
        course_url = None
        result = requests.get(base_url + course_url)

        # 打开一个文件，把 result 的内容写进去
        f = None
        f.write(f.content)

    ### Section 1 Ends ###
    ######################

########################
### Section 2 Starts ###
def download_pages_ic():
    pass

def download_pages_manchester():
    pass

def download_pages_ucl():
    pass

def download_pages_warwick():
    pass
### Section 2 Ends ###
######################


