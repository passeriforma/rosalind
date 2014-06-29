#!/usr/bin/env python

# Length of overlap, what numbers they are (order of suffix, prefix)

import re

f = open('input')
lines = f.read()
f.close()
lines = lines.split('\n')

dna = []
for line in lines:
    string = re.sub('[^GCAT]', '', line)
    if len(string) != 0:
        dna.append(string)

# Calculate overlaps
overlaps = {}
lesshalf = {}
for x in range(len(dna)):
    suffixer = dna[x]
    for i in range(x+1, len(dna)):
        prefixer = dna[i]
        overlap = 0
        p = 0
        s = len(suffixer)-1
        while suffixer[s] == prefixer[p]:
            p += 1
            s -= 1
            overlap += 1
        if overlap > len(suffixer)/float(2):
            if overlap in overlaps:
                overlaps[overlap].append([prefixer, suffixer])
            else:
                overlaps[overlap] = [[prefixer, suffixer]]
        else:
            if overlap in lesshalf:
                lesshalf[overlap].append([prefixer, suffixer])
            else:
                lesshalf[overlap] = [[prefixer, suffixer]]

for x in range(len(dna)-1):
    # Do all of overlaps first, then go for 
    maximum = max(overlaps.keys())
