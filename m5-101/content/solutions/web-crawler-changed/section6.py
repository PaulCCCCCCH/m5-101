# 高效的索引
import pickle
import json
import re
# uncomment this at the first time
# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
from nltk.corpus import stopwords
sw = set(stopwords.words('english'))

# Read pickle File
pkl_file = 'programs.pkl'
f = open(pkl_file, 'rb')
infos = pickle.load(f, encoding='bytes')

word_dict = {}

for key in infos:
    d = json.loads(infos[key])
    words = d['program_desc'].split(' ')
    for w in words:
        # if not stop word
        w = w.lower()
        if w not in sw:
            # get or default 0:{}
            winfo = word_dict.get(w, {"count": 0, "occurrences": set()})
            if d['document_id'] not in winfo["occurrences"]:
                winfo["count"] += 1
                winfo["occurrences"].add(d['document_id'])
            word_dict[w] = winfo

to_save = (infos, word_dict)
pkfile = 'programs_improved.pkl'
with open(pkfile, 'wb') as f:
    pickle.dump(to_save, f)