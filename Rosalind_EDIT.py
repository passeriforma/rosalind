#!/usr/bin/env python

# Given: Two protein strings s and t in FASTA format (each of length at most 1000 aa).
# Return: The edit distance dE(s,t).

import re

f = open('input')
dna = f.read()
f.close()
dna = dna.split('>')
dna1 = dna[1]
dna1 = re.sub("Rosalind_[0-9]*\n", '', dna1)
dna1 = re.sub("\n", '', dna1)
dna2 = dna[2]
dna2 = re.sub('Rosalind_[0-9]*\n', '', dna2)
dna2 = re.sub("\n", '', dna2)

# Input: string, string
# Output: integer of the edit distance
def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
 
    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)
 
    previous_row = xrange(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
 
    return previous_row[-1]

print levenshtein(dna1, dna2)
