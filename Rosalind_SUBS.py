#!/usr/bin/env python

# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

import re

f = open('input')
dna = f.read().split('\n')

DNA = dna[0]

V = [m.start() for m in re.finditer('(?=' + dna[1] + ')', DNA)]
returnV = []
for value in V:
    returnV.append(value + 1)

for i in range(0, len(V)):
    print V[i]+1,
