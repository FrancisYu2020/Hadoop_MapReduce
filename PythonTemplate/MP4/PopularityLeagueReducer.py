#!/usr/bin/env python3
import sys
#TODO
leagues = {}
# input comes from STDIN
for line in sys.stdin:
    # TODO
    line = line.strip()
    page, count = line.split('\t')
    page, count = int(page), int(count)
    leagues[page] = count


#TODO
# print('%s\t%s' % (  ,  )) print as final output
for src in sorted(leagues.keys(), reverse=True):
    rank = 0
    for tgt in leagues:
        if src != tgt and leagues[src] > leagues[tgt]:
            rank += 1
    print('%s\t%s' % (src, rank))