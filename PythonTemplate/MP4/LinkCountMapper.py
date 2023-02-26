#!/usr/bin/env python3
import sys


for line in sys.stdin:
  #TODO
  src, tgts = line.split(': ')
  tgts = tgts[:-1].split(' ') if tgts[-1] == '\n' else tgts.split(' ')
  for tgt in tgts:
    print(tgt)

  # print('%s\t%s' % (  ,  )) pass this output to reducer
