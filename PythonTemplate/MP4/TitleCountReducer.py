#!/usr/bin/env python3
from operator import itemgetter
import sys

# code reference: https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
#TODO
curr_word = None
curr_count = 0

# input comes from STDIN
for line in sys.stdin:
    # TODO
	#if line == 'exit\n':
	#	break
	line = line.strip()
	word, count = line.split('\t', 1)
	try:
		count = int(count)
	except:
		continue
	if curr_word == word:
		curr_count += count
	else:
		if curr_word:
			print("%s\t%s" % (curr_word, curr_count))
		curr_count = count
		curr_word = word
if curr_word == word:
	print("%s\t%s" % (curr_word, curr_count))

# TODO
# print('%s\t%s' % (  ,  )) print as final output
