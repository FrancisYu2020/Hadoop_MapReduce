#!/usr/bin/env python3
import sys

#TODO
pages = {}
# input comes from STDIN
for line in sys.stdin:
    # TODO
    page = line.strip()
    pages[page] = pages.get(page, 0) + 1

# TODO
# print('%s\t%s' % (  ,  )) print as final output
for tgt in pages:
    print('%s\t%s' % (tgt, pages[tgt]))