#!/usr/bin/env python

# Given: A DNA string s in FASTA format (having length at most 100 kbp).
# Return: The 4-mer composition of s.

from re import sub
import sys
from itertools import product
from string import count

f = open('input')
dna = f.read()
f.close()
dna = sub('[^GCAT]', '', dna)

# Calculate all possible 4-mers of ACGT
fourmers = [p for p in product('ACGT', repeat=4)]
for b in range(0, len(fourmers)):
    fourmers[b] = ''.join(fourmers[b])
# Place these in a dict
occurences = {}
for a in fourmers:
    occurences[a] = 0

# Count occurences of each sequence in the DNA string
for x in range(0, len(dna)-3):
    string = dna[x:x+4]
    if string in occurences:
        occurences[string] += 1

# Print!
for i in range(0, len(fourmers)):
    sys.stdout.write(str(occurences[fourmers[i]])+ ' ')
