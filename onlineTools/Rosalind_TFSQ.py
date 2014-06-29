#!/usr/bin/env python

# Given: FASTQ file
# Return: Corresponding FASTA records

from Bio import SeqIO

count = SeqIO.convert(instring, input, outstring, output)
