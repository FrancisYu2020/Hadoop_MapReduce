#!/usr/bin/env python3
import sys


leaguePath = sys.argv[1]
#TODO


with open(leaguePath) as f:
	#TODO
       leagues = set(f.read().split('\n'))

for line in sys.stdin:

       #TODO
       line = line.strip()
       page, count = line.split('\t')
       if page in leagues:
              print(line)

       # print('%s\t%s' % (  ,  )) pass this output to reducer
