from posix import listdir
import requests
from bs4 import BeautifulSoup as bs
import math
import sys, getopt
import re
import os



def re_cleaner(target: str, rep: str) -> str:
    return re.sub("[^0-9a-zA-Z]+", rep, target)

# For Oxford ==============================================================================

# base_url = "https://www.ox.ac.uk/"
# base_dir = "pages/oxford"

# if not os.path.exists(base_dir):
#     os.makedirs(base_dir)

# # Get the root page and extract target urls
# url_pages = requests.get('https://www.ox.ac.uk/admissions/graduate/courses/courses-a-z-listing')

# root_soup = bs(url_pages.text, 'html.parser')
# # print(root_soup.prettify())

# # find by class attr
# course_divs = root_soup.find_all(attrs={"class": "course-title"})

# for div in course_divs:
#     # 从div中取出a然后解析url
#     # 用re直接find_all 符合 ** graduate/courses/ ** 的url更好解释
#     link, degree = div.children
#     degree = degree.strip()
#     if re.search("D", degree) is None and re.match("PG", degree) is None:
#         r = requests.get(base_url + link.get('href'))
#         course_name = link.text
#         with open(os.path.join(base_dir, re_cleaner(course_name+' '+degree, '-')+'.html'), mode='wb') as f:
#             f.write(r.content)
    
#UIUC ==============================================================================

# base_url = "http://catalog.illinois.edu/"
# base_dir = "pages/uiuc"

# if not os.path.exists(base_dir):
#     os.makedirs(base_dir)

# # Get the root page and extract target urls
# url_pages = requests.get('http://catalog.illinois.edu/graduate/')

# root_soup = bs(url_pages.text, 'html.parser')
# # print(root_soup.prettify())

# course_heads = root_soup.find_all("h4")

# for h in course_heads:
#     # 从head中取出a然后解析url, 若有margin left, 则不考虑
#     if 'style' not in h.attrs:
#         # 最多分成两端，此处degree会有冗余, 但生成文件时正确的degree会在最后一个破折号处，优雅
#         major, degree = h.text.split(',' ,1)
#         degree = degree.strip()
#         if re.search("D", degree) is None and re.match("PG", degree) is None:
#             r = requests.get(base_url + h.a['href'])
#             with open(os.path.join(base_dir, re_cleaner(major + ' ' + degree, ' ')+'.html'), mode='wb') as f:
#                 f.write(r.content)


# IC ==============================================================================
# 
# base_url = "https://www.imperial.ac.uk/"
# base_dir = "pages/ic"

# if not os.path.exists(base_dir):
#     os.makedirs(base_dir)

# # Get the root page and extract target urls
# url_pages = requests.get('https://www.imperial.ac.uk/study/pg/courses/')

# root_soup = bs(url_pages.text, 'html.parser')

# # find by class attr
# course_lis = root_soup.find_all(attrs={"class": "course"})

# for li in course_lis:
#     degree = li.a.contents[5].contents[1].strip()
#     if re.match("D", degree) is None and re.match("PG", degree) is None:
#         url = base_url + li.a['href']
#         major = li.a['title']
#         r = requests.get(url)
#         with open(os.path.join(base_dir, re_cleaner(major + ' ' + degree, '-')+'.html'), mode='wb') as f:
#             f.write(r.content)

# Make Index ==============================================================================
import json
import pickle

def clean_html(soup: bs):
    ss = soup.find_all('script')
    for s in ss:
        s.decompose()
    return re_cleaner(soup.get_text(), ' ')

data = {}

pages_path = os.path.join(os.getcwd(), 'pages')
idx = 1
for school in os.listdir(pages_path):
    school_path = os.path.join(pages_path, school)
    for filename in os.listdir(school_path):
        filepath = os.path.join(school_path, filename)
        program, degree_html = filename.rsplit('-', 1)
        degree,_ = degree_html.split('.', 1)
        print(filename)
        with open(filepath) as f:
            soup = bs(f, 'html.parser')
            desc = clean_html(soup)
            jsobj = json.dumps({"document_id": idx, "school_name": school, "program_name": program, "degree": degree, "file_path": filepath, "program_desc": desc})
            data[idx] = jsobj
        idx += 1

pkfile = 'programs.pkl'
with open(pkfile, 'wb') as f:
    pickle.dump(data, f)
        

