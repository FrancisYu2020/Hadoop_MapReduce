#!/usr/bin/env python3
import sys


#TODO
pages = {}
# pages1 = {}

for line in sys.stdin:
    # TODO
    line = line.strip()
    page, link_type = line.split('\t')
    page = int(page)
    if page not in pages:
      pages[page] = 0
    if link_type == 'IN':
       pages[page] += 1
    # print(line)
    
# #TODO
# # print(xx) print as final output
for page in sorted(pages.keys()):
   if pages[page] == 0:
      print(page)