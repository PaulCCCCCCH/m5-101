import pickle
import re

########################
### Section 6 Starts ###


# 重新读取所有 HTML 页面，或者使用之前建立好的索引（programs.pkl）。可以适当使用之前的代码。
programs = None

# 初始化新的字典，用于保存新的索引
word_dict = {}
program_info = {}

### 
### 在这里建立新的索引
###


# 保存新的索引
to_save = (infos, word_dict)
pkfile = 'programs_improved.pkl'
with open(pkfile, 'wb') as f:
    pickle.dump(to_save, f)

### Section 6 Ends ###
######################
