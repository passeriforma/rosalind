#!/usr/bin/env python

# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
# Return: The adjacency list corresponding to O3. You may return edges in any order.

import re

f = open('input')
lines = f.read()
f.close
lines = lines.split('>')
lines.remove('')

dna = []
for i in range(0, len(lines)):
    dna.append(re.sub('[^GCAT]', '', lines[i]))

prefixes = {}
suffixes = {}

for i in range(0, len(dna)):
    strand = dna[i]
    prefix = strand[:3]
    suffix = strand[len(strand)-3:]
    name = lines[i].split()[0]
    if prefix in prefixes:
        prefixes[prefix].append(name)
    else:
        prefixes[prefix] = [name]
    if suffix in suffixes:
        suffixes[suffix].append(name)
    else:
        suffixes[suffix] = [name]


for suff in suffixes:
    try:
        suffix = suffixes[suff]
        prefix = prefixes[suff]
        if len(prefix) == 0:
            continue
        else:
            for suf in suffix:
                for pref in prefix:
                    if pref != suf:
                        print suf + ' ' + pref
    except:
        continue
