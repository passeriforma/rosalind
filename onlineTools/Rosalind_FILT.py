#!/usr/bin/env python

# Given: A quality threshold value q, percentage of bases p, and set of FASTQ entries.
# Return: Number of reads in filtered FASTQ entries

from Bio import SeqIO

f = open('input')
values = f.readline().split()
quality_threshold = int(values[0])
percent_bases = int(values[1])
f.close()

below_limit = 0
input_length = 0

with open('input') as input_data:
    for record in SeqIO.parse(input_data, 'fastq'):
        input_length += 1
        phred = record.letter_annotations["phred_quality"]
        threshold_num = len(phred) - len(phred)*(float(percent_bases/float(100)))
        for base in phred:
            if base < quality_threshold:
                threshold_num -= 1
                if threshold_num < 0: #below the limit
                    below_limit += 1
                    break

print input_length - below_limit
