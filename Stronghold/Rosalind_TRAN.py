#!/usr/bin/env python

# Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
# Return: The transition/transversion ratio R(s1,s2).

import sys
import re

f = open('input')
lines = f.read()
f.close()
lines = lines.split('>')
dna1 = lines[1]
dna1 = re.sub('[^GACT]', '', dna1)
dna2 = lines[2]
dna2 = re.sub('[^GACT]', '', dna2)

transitions = 0
transversions = 0

# Calculate transition and transversion numbers
for x in range(0, len(dna1)):
    char1 = dna1[x]
    char2 = dna2[x]
    # Transitions
    if char1 == 'A' and char2 == 'G':
         transitions += 1
    elif char1 == 'G' and char2 == 'A':
         transitions += 1
    elif char1 == 'C' and char2 == 'T':
         transitions += 1
    elif char1 == 'T' and char2 == 'C':
         transitions += 1
    # Transversions
    elif char1 == 'A' and char2 == 'C':
        transversions += 1
    elif char1 == 'C' and char2 == 'A':
        transversions += 1
    elif char1 == 'A' and char2 == 'T':
        transversions += 1
    elif char1 == 'T' and char2 == 'A':
        transversions += 1
    elif char1 == 'C' and char2 == 'G':
        transversions += 1
    elif char1 == 'G' and char2 == 'C':
        transversions += 1
    elif char1 == 'G' and char2 == 'T':
        transversions += 1
    elif char1 == 'T' and char2 == 'G':
        transversions += 1

print transitions/float(transversions)

