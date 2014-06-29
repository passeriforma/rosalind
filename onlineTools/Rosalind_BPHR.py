#!/usr/bin/env python 

# Given: FASTQ file, quality threshold q
# Return: Number of positions where mean base quality falls below given threshold
 
from Bio import SeqIO 
 
f = open('input') 
quality = int(f.readline())
f.close() 
 
below_limit = 0 
bases = []
strings = 0

with open('input') as input_data: 
    for record in SeqIO.parse(input_data, 'fastq'): 
        strings += 1
        phred = record.letter_annotations["phred_quality"] 
        for num in range(0, len(phred)):
            try:
                bases[num] += phred[num]
            except:
                bases.append(phred[num])

for x in bases:
    if x/float(strings) < quality:
        below_limit += 1

print below_limit
