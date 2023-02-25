#!/usr/bin/env python3
import sys

max_word = []

# input comes from STDIN
for line in sys.stdin:
    # TODO
	_, pair = line.split('\t', 1)
	count, word = pair.split(',')
	# count, word = line.split('\t', 1)
	try:
		count = int(count)
	except:
		continue
	if len(max_word) < 5:
		max_word.append((word, count))
	else:
		min_count, min_pos = float('inf'), -1
		for i in range(len(max_word)):
			curr_word, curr_count = max_word[i]
			if curr_count < min_count or (curr_count == min_count and curr_word < max_word[min_pos][0]):
				min_count, min_pos = curr_count, i
		if count > min_count or (count == min_count and word > max_word[min_pos][0]):
			max_word[min_pos] = (word, count)
max_word.sort(key=lambda x:x[1])
for i in range(len(max_word)):
	print('%s\t%s' % max_word[i])
