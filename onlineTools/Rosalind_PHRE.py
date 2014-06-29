#!/usr/bin/env python

# Given: A quality threshold, along with FASTQ entries for multiple reads.
# Return: The number of reads whose average quality is below the threshold.

from Bio import SeqIO

lowaverage = 0

with open('input') as input_data:
    for record in SeqIO.parse(input_data, 'fastq'):
        phred = record.letter_annotations["phred_quality"]
        average = sum(phred)/float(len(phred))
        if average < 23:
            print(str(record.id) + ': ' + str(average))
            lowaverage += 1

print lowaverage
