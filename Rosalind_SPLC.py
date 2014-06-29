#!/usr/bin/env python

# Given: A DNA string  (of length at most 1 kbp) and a collection of substrings of  acting as introns. All strings are given in FASTA format.
# Return: A protein string resulting from transcribing and translating the exons of . (Note: Only one solution will exist for the dataset provided.)

import re
import sys

f = open('input')
lines = f.read()
lines = lines.split('>')

dna = lines[1]
dna = re.sub('[^CGAT]', '', dna)

# Remove introns from DNA string
for x in range(2, len(lines)):
    string = lines[x]
    string = re.sub('[^CGAT]', '', string)
    #remove intron
    if string in dna:
        dna = re.sub(string, '', dna)

# Convert DNA to protein and print
codontable = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'', 'TAG':'',
'TGC':'C', 'TGT':'C', 'TGA':'', 'TGG':'W',
}

proteinsequence = ''
for n in range(0, len(dna),3):
    if dna[n:n+3] in codontable:
        proteinsequence = codontable[dna[n:n+3]]
        sys.stdout.write(proteinsequence)
print("")
