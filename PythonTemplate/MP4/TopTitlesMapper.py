#!/usr/bin/env python3
import sys


# TODO



for line in sys.stdin:

       #TODO
	word, count = line.split('\t', 1)
	try:
		count = int(count)
	except:
		continue

	print('%s\t%s' % (count,word))
#TODO
# print('%s\t%s' % (count,  )) 
