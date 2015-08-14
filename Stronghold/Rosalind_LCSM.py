#!/usr/bin/env python

# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

import re

# Import and manipulate the given DNA strings
f = open('input')
dna = f.read()
f.close()
dna = dna.split('>') # Number 0 is an empty string
for a in range(0, len(dna)):
    dna[a] = re.sub('[^GCAT]', '', dna[a])

first_string = dna[1]
other_strings = dna[2:]
length = len(dna[1])
string = ''

#starts with the whole string and decrements from both ends
for i in range(1, length):
    for x in range(length, i+len(string), -1):
        s1 = first_string[i:x]
        match = True
        for s2 in other_strings:
            if s1 not in s2:
                match = False
                break
        if match:
            string = s1
            break

print string
