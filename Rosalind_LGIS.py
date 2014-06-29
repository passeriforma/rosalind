#!/usr/bin/env python

# Given: A positive integer n≤10000 followed by a permutation π of length n.
# Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

import sys

f = open('input')
inputs = f.read()
f.close()

inputs = inputs.split('\n')
length = int(inputs[0])
seq = inputs[1].split()
for num in range(0, length):
    seq[num] = int(seq[num])

# Calculate the longest increasing subsequence
def longest_increasing_subsequence(d):
    'Return one of the L.I.S. of list d'
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], key=len) 
                  + [d[i]])
    return max(l, key=len)

# Longest increasing
inc = longest_increasing_subsequence(seq)
for char in inc:
    sys.stdout.write(str(char) + ' ')
print ''
dec = longest_increasing_subsequence(list(reversed(seq)))
for char in reversed(dec):
        sys.stdout.write(str(char) + ' ')
print ''

