#!/usr/bin/env python

# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.

f = open('input')
dna = f.read()

#reverse order of string
reverse_dna = dna[::-1]

#print reverse_dna

half_complement = reverse_dna.replace('A', 'X').replace('T', 'A').replace('X', 'T')

full_complement = half_complement.replace('C', 'Y').replace('G', 'C').replace('Y', 'G')

print full_complement
