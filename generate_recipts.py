  1 import random
  2 import os
  3 import json
  4
  5 count = int(os.getenv("FILE_COUNT") or 100)
  6
  7 with open ('/usr/share/dict/words') as f:
  8     words = f.readlines()
  9 matches = []
 10
 11 for word in words:
 12     matches.append(word.strip())
 13
 14 for identifier in range(count):
 15     amount = random.uniform(1.0, 1000)
 16     content = {'topic': random.choice(matches), 'value': "%.2f" % amount }
 17
 18     with open(f'./new/receipt-{identifier}.json', 'w' ) as f:
 19         json.dump(content, f)
