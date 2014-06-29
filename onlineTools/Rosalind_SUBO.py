#!/usr/bin/env python

# Given: Two DNA strings s and t in FASTA format that share some short inexact repeat r of 32-40 bp. By "inexact" we mean that r may appear with slight modifications (each repeat differ by ≤3 changes/indels).
# Return: The total number of occurrences of r as a substring of s, followed by the total number of occurrences of r as a substring of t.

from Bio import SeqIO

with open('input') as input_data:
    dna = [fasta.seq for fasta in SeqIO.parse(input_data, 'fasta')]

# Find r from the given site; its the one with a 100% match between strings
r = 'TAGCGCGAACAACCCCTGCATCGTCATTCGAACGGGCAGG'
print len(r)

def HammingDistance(str1, str2):
        diffs = 0
        for ch1, ch2 in zip(str1, str2):
                if ch1 != ch2:
                        diffs += 1
        return diffs
for x in range(0, 2):
    count = 0
    stringx = dna[x]
    for i in range(0, len(stringx)-len(r)):
        string = stringx[i:i+len(r)]
        if HammingDistance(r, string) <= 3:
            count += 1
    print count
