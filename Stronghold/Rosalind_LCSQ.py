#!/usr/bin/env python

# Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.
# Return: A longest common subsequence of s and t. (If more than one solution exists, you may return any one.)

import re

f = open('input')
dna = f.read()
f.close()
dna = dna.split('>')
dna1 = dna[1]
dna1 = re.sub('[^GCAT]', '', dna1)
dna2 = dna[2]
dna2 = re.sub('[^GCAT]', '', dna2)

lengths = [[0 for j in range(len(dna2)+1)] for i in range(len(dna1)+1)]
for i, x in enumerate(dna1):
    for j, y in enumerate(dna2):
        if x == y:
            lengths[i+1][j+1] = lengths[i][j] + 1
        else:
            lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])

# Read substring
result = ''
x = len(dna1)
y = len(dna2)
while x != 0 and y != 0:
    # Deal with double of letters
    if lengths[x][y] == lengths[x-1][y]:
        x -= 1
    elif lengths[x][y] == lengths[x][y-1]:
        y -= 1
    elif dna1[x-1] == dna2[y-1]:
        result = dna1[x-1] + result
        x -= 1
        y -= 1

print result
