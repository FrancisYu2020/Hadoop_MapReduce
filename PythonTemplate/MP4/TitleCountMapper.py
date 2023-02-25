#!/usr/bin/env python3

import sys
import string
import re

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]


# TODO
with open(stopWordsPath) as f:
    # TODO
    stopWords = f.read().split('\n')

#TODO 
with open(delimitersPath) as f:
    # TODO
    delimiters = f.read()

for line in sys.stdin:
  
    # TODO
    clean = ''
    line = line[:-1].lower() if line[-1] == '\n' else line.lower()
    for char in line:
        clean += ' ' if char in delimiters else char
    line = clean.split(' ')
    for word in line:
        if word != '' and word not in stopWords:
            print('%s\t%s' % (word, 1))
            # yield (word, 1)
    # print('%s\t%s' % (  ,  )) pass this output to reducer


