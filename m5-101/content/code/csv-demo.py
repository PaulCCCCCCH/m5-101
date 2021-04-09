#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[2]:


from faker import Faker
import random
import numpy as np
import datetime
import time


# In[3]:


csv_file = csv.reader(open('../txt_files/eshop-data.csv'))
lines = [line for line in csv_file]


# In[4]:


fake = Faker(locale="zh_CN")


# In[5]:


NUM_TO_FAKE = 1000
BASE_ORDER_ID = 81417556230000


# In[6]:


订单编号 = np.random.permutation(range(BASE_ORDER_ID, BASE_ORDER_ID + 10 * NUM_TO_FAKE))[:NUM_TO_FAKE]


# In[7]:


all_states = ["已完成", "已关闭"]
订单状态 = [all_states[random.randint(0, 1)] for _ in range(NUM_TO_FAKE)]


# In[8]:


def get_date_pair():
    date1 = fake.date_time_between(
        start_date=datetime.datetime.strptime('2021-01-20 23:59:59', "%Y-%m-%d %H:%M:%S"), 
        end_date=datetime.datetime.strptime('2021-02-01 23:59:59', "%Y-%m-%d %H:%M:%S")
    )
    date2 = fake.date_time_between(
        start_date=datetime.datetime.strptime('2021-01-20 23:59:59', "%Y-%m-%d %H:%M:%S"), 
        end_date=datetime.datetime.strptime('2021-02-01 23:59:59', "%Y-%m-%d %H:%M:%S")
    )
    if date1 > date2:
        return date2, date1
    return date1, date2
    
下单发货时间 = [get_date_pair() for _ in range(NUM_TO_FAKE)]
下单时间 = [datetime.datetime.strftime(p[0], "%Y-%m-%d %H:%M:%S") for p in 下单发货时间]
发货时间 = [datetime.datetime.strftime(p[1], "%Y-%m-%d %H:%M:%S") for p in 下单发货时间]


# In[9]:


支付方式 = ["借记卡"] * NUM_TO_FAKE


# In[10]:


all_products = [("哇鸥乐意优享礼盒", "2101"), ("哇鸥心意优享礼盒", "2102"), ("哇鸥顺意优享礼盒", "2110")]
商品型号编码 = [all_products[random.randint(0, 2)] for _ in range(NUM_TO_FAKE)]
商品型号 = [p[0] for p in 商品型号编码]
商品编码 = [p[1] for p in 商品型号编码]


# In[11]:


商品件数 = [int(np.random.exponential(2)) + 1 for _ in range(NUM_TO_FAKE)]


# In[12]:


prices = {
    "2101": 445,
    "2102": 667,
    "2110": 1118
}
商品金额 = [prices[i] * count for i, count in zip(商品编码, 商品件数)]


# In[13]:


all_discounts = [0, 0, 0, 0, 0, 0, 0, 20, 20, 30, 40]
优惠金额 = [all_discounts[random.randint(0, len(all_discounts) - 1)] for _ in range(NUM_TO_FAKE)]


# In[14]:


实付金额 = [p - d for p, d in zip(商品金额, 优惠金额)]


# In[15]:


收货人姓名 = [fake.name() for _ in range(NUM_TO_FAKE)]


# In[16]:


收货人手机 = [fake.phone_number() for _ in range(NUM_TO_FAKE)]


# In[17]:


收货人地址 = [fake.address() for _ in range(NUM_TO_FAKE)]


# In[18]:


all_data = [订单编号, 订单状态, 下单时间, 发货时间, 支付方式, 商品型号, 商品编码, 商品件数, 商品金额, 优惠金额, 实付金额, 收货人姓名, 收货人手机, 收货人地址]


# In[19]:


csv_content = zip(*all_data)


# In[20]:


with open("sales.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(['订单编号', '订单状态', '下单时间', '发货时间', '支付方式', '商品型号', '商品编码', '商品件数', '商品金额', '优惠金额', '实付金额', '收货人姓名', '收货人手机', '收货人地址'])
    for t in csv_content:
        writer.writerow(list(t))

