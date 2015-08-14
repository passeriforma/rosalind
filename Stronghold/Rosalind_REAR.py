#!/usr/bin/env python

# Given: A collection of at most 5 pairs of permutations, all of which have length 10.
# Return: The reversal distance between each permutation pair.

import sys

f = open('input')
lines = f.read()
f.close()

lines = lines.split('\n')

for i in range(0, (len(lines)/3)):
    line1 = lines[i*3].split()
    line2 = lines[i*3+1].split()
    if line1 == line2:
	sys.stdout.write('0 ')
    else:
        

print ''
