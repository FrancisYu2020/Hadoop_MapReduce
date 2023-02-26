#!/usr/bin/env python3
import sys

top = []

# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.strip()
    # print(line)
    _, page, count = line.split('\t')
    count = int(count)
    if len(top) < 10:
        top.append((count, page))
        top.sort(reverse=True)
    else:
        for i in range(10):
            if count > top[i][0]:
                top.insert(i, (count, page))
                top.pop()
                break
    # print('%s\t%s' % (  ,  )) print as final output
for pair in reversed(top):
    count, page = pair
    print('%s\t%s' % (page, count))