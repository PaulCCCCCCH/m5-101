# search_key_word_improved
import pickle
import json
import re

# Read pickle File
pkl_file = 'programs_improved.pkl'
f = open(pkl_file, 'rb')
infos, word_dict = pickle.load(f, encoding='bytes')
print(len(infos))

# Search

programs = []
keyword = input('Improved ! What ru looking for : ')
keyword = keyword.lower()
word_info = word_dict.get(keyword, None)
if word_info is not None:
    for i in word_info['occurrences']:
        programs += [json.loads(infos[i])['program_name']]
print('\n'.join('{}: {}'.format(idx+1, prog) for idx, prog in enumerate(programs)))
