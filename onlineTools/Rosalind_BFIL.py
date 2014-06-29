#!/usr/bin/env python

# Given: FASTQ file, quality cut-off value q, Phred33 quality score assumed.
# Return: FASTQ file trimmed from the both ends (removed leading and trailing bases with quality lower then q)

from Bio import SeqIO
import sys

f = open('input')  
quality = int(f.readline())
f.close()

with open('input') as input_data:
    for record in SeqIO.parse(input_data, 'fastq'):
        seq_rec = record
        phred = seq_rec.letter_annotations["phred_quality"]
        while phred[0] < quality:
            seq_rec = seq_rec[1:]
            phred = seq_rec.letter_annotations["phred_quality"]
        while phred[len(seq_rec)-1] < quality:
            seq_rec = seq_rec[:len(seq_rec)-1]
            phred = seq_rec.letter_annotations["phred_quality"]
        sys.stdout.write(seq_rec.format("fastq"))
