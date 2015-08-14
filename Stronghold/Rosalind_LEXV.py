#!/usr/bin/env python

# Given: A permutation of at most 12 symbols defining an ordered alphabet 𝒜 and a positive integer n (n≤4).
# Return: All strings of length at most n formed from 𝒜, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)

from itertools import product

f = open('input')
lines = f.read()
f.close()
lines = lines.split('\n')

alphabet = ['*'] + lines[0].split()
length = int(lines[1])

permutations = []
for item in product(alphabet, repeat=length):
    if '*' not in item:
        permutations.append(''.join(item))
        item = ''.join(item)
    else:
        # Items with only trailing * should be added 
        for i in range(1, length):
            if ''.join(item[i:length]) == '*'*(length-i) and '*' not in item[:i]:
                permutations.append(''.join(item).replace('*',''))
                item = ''.join(item).replace('*', '')

for a in range(0, len(permutations)):
    print permutations[a]
