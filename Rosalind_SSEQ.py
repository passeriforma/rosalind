#!/usr/bin/env python

# Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
# Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.

import sys
import re
import string

f = open('input')
dna = f.read()
f.close()

dna = dna.split('>')
dnastring = dna[1]
dnastring = re.sub('[^GCAT]', '', dnastring)
symbols = dna[2]
symbols = re.sub('[^GCAT]', '', symbols)

index = []
currentindex = 0

for char in symbols:
    currentindex = dnastring.find(char, currentindex)+1
    index.append(currentindex)

for number in index:
    sys.stdout.write(str(number) + ' ')

print('')
