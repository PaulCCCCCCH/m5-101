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

# 搜索所有 program 的 program_description 字段，找出包含关键词的项目，以一定格式 print
programs = []
print(programs)