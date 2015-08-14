#!/usr/bin/env python

# Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.
# Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.

import math
import sys

# Read in file
f = open('input')
files = f.read()
f.close()

files = files.split('\n')
dna = files[0]
gccontents = files[1].split()

for x in range(0, len(gccontents)):
    percent = 1
    chanceGC = float(gccontents[x])/2.0
    chanceAT = (1 - float(gccontents[x]))/2.0
    for i in range(0, len(dna)):
        nucleotide = dna[i]
        if nucleotide == 'C' or nucleotide == 'G':
            percent = percent*chanceGC
        if nucleotide == 'A' or nucleotide == 'T':
            percent = percent*chanceAT
    percent = math.log10(percent)
    sys.stdout.write(str(round(percent, 3)) + ' ')

print("")
