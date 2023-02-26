#!/usr/bin/env python3
import sys

total = 0
min_count = float('inf')
max_count = 0
word_count = 0
x_squared = []

for line in sys.stdin:
    # TODO
    line = line.strip()
    _, count = line.split('\t')
    count = int(count)
    word_count += 1
    total += count
    min_count = min(min_count, count)
    max_count = max(max_count, count)
    x_squared.append(count)
    # print('%s\t%s' % (  ,  )) pass this output to reducer
mean = total // word_count
var = 0
for t in x_squared:
    var += (t - mean)**2
var //= word_count
print('%s\t%s' % ('Mean', mean))
print('%s\t%s' % ('Sum', total))
print('%s\t%s' % ('Min', min_count))
print('%s\t%s' % ('Max', max_count))
print('%s\t%s' % ('Var', var))