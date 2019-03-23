  1 import os
  2 import glob
  3 import json
  4 import shutil
  5
  6 try:
  7     os.mkdir('./processed')
  8 except OSError:
  9     print("'processed' directory olready exists")
 10
 11 subtotal = 0.0
 12
 13 for path in glob.iglob('./new/receipt-[0-9]*.json'):
 14     with open(path) as f:
 15         content = json.load(f)
 16         subtotal += float(content['value'])
 17     destination = path.replace('new', 'processed')
 18     shutil.move(path, destination)
 19     print(f"moved '{path}' to '{destination}'")
 20
 21 print(f"Receipt subtotal: ${round(subtotal, 2)}")
