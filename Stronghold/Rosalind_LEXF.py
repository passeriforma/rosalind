#!/usr/bin/env python

# Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).
# Return: All strings of length n that can be formed from the alphabet, ordered lexicographically.

import itertools

f = open('input')
lines = f.read()
f.close()
lines = lines.split('\n')

alphabet = lines[0].split()
length = int(lines[1])

def permu(s,n):
    permu_l = [p for p in itertools.product(s, repeat=n)]
    for x in permu_l:
        print ''.join(list(x))

permu(alphabet, length)
