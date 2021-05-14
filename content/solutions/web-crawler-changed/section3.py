import json
import pickle
from bs4 import BeautifulSoup as bs

# 可以使用这个函数替换非英文字符
def re_cleaner(target: str, rep: str) -> str:
    return re.sub("[^0-9a-zA-Z]+", rep, target)

# 调用这个函数，可以清除 HTML 文件中所有的 script 标签
def clean_html(bs):
    ss = soup.find_all('script')
    for s in ss:
        s.decompose()
    return re_cleaner(soup.get_text(), ' ')

########################
### Section 3 Starts ###
pages_path = os.path.join(os.getcwd(), 'pages')
idx = 1

# 初始化一个字典，用于保存所有索引数据
data = {}

# 对于每一所大学：
for school in os.listdir(pages_path):
    school_path = os.path.join(pages_path, school)
    # 对于每一所大学的所有项目文件：
    for filename in os.listdir(school_path):
        filepath = os.path.join(school_path, filename)

        # 打开这个文件：
        with open(filepath) as f:
            # 用 beautiful soup 解析它
            soup = bs(f, 'html.parser')
            # 使用 clean_html 把它变得干净些
            description = clean_html(soup)

            # 请提取对应的内容
            info = {
                "document_id": idx,
                "school_name": None,
                "program_name": None,
                "degree": None,
                "file_path": None,
                "program_description": description,
            }
            data[idx] = info
        idx += 1

# 使用 `pickle` 保存文件
pkfile = 'programs.pkl'
with open(pkfile, 'wb') as f:
    pickle.dump(data, f)

### Section 3 Ends ###
######################
