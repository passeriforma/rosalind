#!/usr/bin/env python

# Given: A protein string of length at most 1000 aa.
# Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

import sys

protein_string = sys.stdin.read()

a=0
b=1
rna_types = 3 #stop codon; at least 3 for any

while protein_string[b-1] != '\n':
	amino_acid = protein_string[a:b]
	amino_acid = amino_acid.strip()
	print amino_acid
#	if amino_acid == 'W' or amino_acid == 'M':
#		pass
	if amino_acid == 'F' or amino_acid == 'Y' or amino_acid == 'C' or amino_acid == 'H' or amino_acid == 'Q' or amino_acid == 'N' or amino_acid == 'K' or amino_acid == 'D' or amino_acid == 'E':
		rna_types = rna_types*2
	elif amino_acid == 'I':
		rna_types = rna_types*3
	elif  amino_acid == 'P' or amino_acid == 'T' or amino_acid == 'V' or amino_acid == 'A' or amino_acid == 'G':
		rna_types = rna_types*4
#		print rna_types
	elif amino_acid == 'L' or amino_acid == 'S' or amino_acid == 'R':
		rna_types = rna_types*6
	else:
		pass
#print "What went wrong here? This isnt an amino acid!"
	a = a+1
	b = b+1

rna_types = rna_types%1000000

print rna_types
