#!/usr/bin/env python

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).

import sys

input_dna = sys.stdin.read().split('\n')

strand_one = input_dna[0]
strand_two = input_dna[1]

#print strand_one

length = len(strand_one)
a = 0
hamming_distance = 0

while a < length:
	if strand_one[a] == strand_two[a]:
		pass
	else:
		hamming_distance = hamming_distance + 1
	a = a+1

print hamming_distance
