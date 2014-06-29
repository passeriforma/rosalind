#!/usr/bin/env python

# Given: Two protein strings s and t in FASTA format (with each string having length at most 1000 aa).
# Return: The edit distance dE(s,t) followed by two augmented strings s′ and t′ representing an optimal alignment of s and t.

import re

f = open('input')
dna = f.read()
f.close
dna = dna.split('>')
dna1 = dna[1]
dna1 = re.sub('Rosalind_[0-9]*\n', '', dna1)
dna1 = re.sub('\n', '', dna1)
dna2 = dna[2]
dna2 = re.sub('Rosalind_[0-9]*\n', '', dna2)
dna2 = re.sub('\n', '', dna2)

# Input: string (short), string (long)
# Prints edit distance and edited strings
def editdistance(s, t):
    edit = 0
    shorter = s
    longer = t
    for x in range(0, len(longer)):
        if x >= len(shorter):
            for a in range(len(shorter), len(longer)):
                shorter = shorter + '-'
                edit += 1
            break
        elif shorter[x] != longer[x]:
            if len(shorter)-1 <= x:
                edit += 1
                continue
            else:
                if shorter[x] == longer[x+1]:
                    shorter = shorter[0:x] + '-' + shorter[x:]
                elif shorter[x+1] == longer[x]:
                    longer = longer[0:x] + '-' + longer[x:]
                edit += 1
    print edit
    print shorter
    print longer

if len(dna1) < len(dna2):
    editdistance(dna1, dna2)
else:
    editdistance(dna2, dna1)
