#!/usr/bin/env python3
import sys


# TODO



for line in sys.stdin:

    #TODO
	word, count = line.split('\t', 1)
	# try:
	# 	count = int(count)
	# except:
	# 	continue
	count = int(count)

	print('%s\t%s,%s' % ('None',count,word))
#TODO
# print('%s\t%s' % (count,  )) 
