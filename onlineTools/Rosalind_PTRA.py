#!/usr/bin/env python

# Given: A DNA string s of length at most 10 kbp, and a protein string translated by s.
# Return: The index of the genetic code variant that was used for translation. (If multiple solutions exist, you may return any one.)

from Bio.Seq import translate

f = open('input')
lines = f.read()
f.close()

lines = lines.split('\n')
dna = lines[0]
protein = lines[1]

# List of all possible ncbi tables
ncbi = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15]

for x in ncbi: 
    if translate(dna, stop_symbol="", table=x) == protein:
        print x
        break
