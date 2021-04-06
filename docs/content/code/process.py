# encoding=utf-8
# -*- coding: utf-8 -*-
'''
Author: Chonghan Chen (paulcccccch@gmail.com)
-----
Last Modified: Tuesday, 6th April 2021 11:52:31 am
Modified By: Chonghan Chen (paulcccccch@gmail.com)
-----
Copyright (c) 2021 IceWould Information Technology Co., Ltd.
'''
import csv # 用来处理 csv 文件

########################
### Section 1 Starts ###

def read_csv(filename):
    """
    Args:
        filename 需要读取的 csv 文件名
    """
    f = open(filename)  # 使用 open 函数打开文件，得到一个未解码的文件 f。
    return csv.reader(f)  # 用 csv 这个库来解码文件。


def main():  # 这个 python 文件的主函数
    csv_content = read_csv('./sales.csv')
    lines = []
    for line in csv_content:
        lines.append(line) 
    print(lines[0])  # 之后可以注释掉。打印表头。
    print(lines[1:4])  # 之后可以注释掉。打印数据的前几行。

    revenue = calculateRevenue()
    reduction = calculateStockReduction()
    slowedUsers = getSlowedDelivery()
    # sendEmails()
    autoDownload()

#### Section 1 Ends ####
########################


########################
### Section 2 Starts ###
def calculateRevenue():

    ########################
    ### YOUR CODE STARTS ###
    return None

    #### YOUR CODE ENDS ####
    ########################

def calculateStockReduction():
    
    ########################
    ### YOUR CODE STARTS ###
    return None

    #### YOUR CODE ENDS ####
    ########################

#### Section 2 Ends ####
########################


########################
### Section 3 Starts ###
def getSlowedDelivery():

    ######################## 
    ### YOUR CODE STARTS ###
    return None

    #### YOUR CODE ENDS ####
    ########################

#### Section 3 Ends ####
########################


########################
### Section 4 Starts ###

import smtplib  # Python 自带的用于发送邮件的库
from email.mime.text import MIMEText

def sendEmails():

    ########################
    ### YOUR CODE STARTS ###

    # 在这里填写邮件的题目
    subject = "销售数据汇总"

    # 在这里填写你的邮箱地址
    sender = '576140292@qq.com'

    # 在这里填写所有收件人
    receivers = ['2658715614@qq.com', "zy22098@nottingham.edu.cn"]

    # 在这里组装你的邮件内容
    content = "这是测试邮件的内容"

    # 在这里填写授权码
    code = 'ixduhgcdewjdbegd'

    # 创建消息
    msg = MIMEText(content)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = str(receivers)

    try:
        connection = smtplib.SMTP_SSL("smtp.qq.com", 465)
        connection.login(sender, code)
        connection.sendmail(sender, receivers, msg.as_string())
        print("发送成功")
    except Exception as e:
        print("发送失败")
        print(str(e))
    finally:
        connection.quit()

    #### YOUR CODE ENDS ####
    ########################

#### Section 4 Ends ####
########################



########################
### Section 5 Starts ###
import requests
import datetime

def autoDownload():
    url = 'https://icewould.com/m5-101/sales-data'
    print(str(datetime.datetime.now()) + ": 正在下载最新销售数据...")
    ########################
    ### YOUR CODE STARTS ###

    result = requests.get(url)
    with open('sales.csv', 'wb') as f:
        f.write(result.content)
        print(str(datetime.datetime.now()) + ": 数据下载完成！")

    return None

    #### YOUR CODE ENDS ####
    ########################

#### Section 5 Ends ####
########################

if __name__ == "__main__":
    import time
    while True:
        main()
        time.sleep(30)
