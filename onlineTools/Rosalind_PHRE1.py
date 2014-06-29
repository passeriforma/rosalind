#!/usr/bin/env python

# Given: A quality threshold, along with FASTQ entries for multiple reads.
# Return: The number of reads whose average quality is below the threshold.

from Bio import SeqIO

threshold = 28
reads = {"@Rosalind_0041": 'GGCCGGTCTATTTACGTTCTCACCCGACGTGACGTACGGTCC+6.3536354;.151<211/0?::6/-2051)-*"40/.,+%)', "@Rosalind_0041": 'TCGTATGCGTAGCACTTGGTACAGGAAGTGAACATCCAGGAT+AH@FGGGJ<GB<<9:GD=D@GG9=?A@DC=;:?>839/4856', "@Rosalind_0041": 'ATTCGGTAATTGGCGTGAATCTGTTCTGACTGATAGAGACAA+@DJEJEA?JHJ@8?F?IA3=;8@C95=;=?;>D/:;74792.]'}

for read in reads:
	print read.letter_annotations["phred_quality"]
