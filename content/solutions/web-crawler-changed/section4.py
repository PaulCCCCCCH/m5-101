import pickle
import json
import re

# 读取之前建立的索引（一个 pickle 文件）
pkl_file = 'programs.pkl'
f = open(pkl_file, 'rb')
infos = pickle.load(f, encoding='bytes')
print("数据库中一共有 {} 个项目的信息".format(len(infos)))


# 提示用户数据项目名的关键词
keyword = input('请输入你想搜索的一个关键词: ')

# 搜索所有符合要求的 program，最终以一定的格式 print 出来给用户
programs = []
print(programs)