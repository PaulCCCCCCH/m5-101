import pickle
import json
import re

# Read pickle File
pkl_file = 'programs.pkl'
f = open(pkl_file, 'rb')
infos = pickle.load(f, encoding='bytes')
print(len(infos))

# Search

##########################
## 提示字典套 json 的问题
##########################

programs = []
keyword = input('What ru looking for : ')
for key in infos:
    d = json.loads(infos[key])
    if re.search(keyword, d['program_name'], re.IGNORECASE) is not None:
        programs += [d['program_name']]
print('\n'.join('{}: {}'.format(idx+1, prog) for idx, prog in enumerate(programs)))
