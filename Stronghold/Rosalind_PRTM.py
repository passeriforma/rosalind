#!/usr/bin/env python

# Given: A protein string P of length at most 1000 aa.
# Return: The total weight of P. Consult the monoisotopic mass table.

import sys

protein = sys.stdin.read()

a = 0
b = 1
weight = 0
while protein[b-1] != '\n':
	amino_acid = protein[a:b]
	print amino_acid
	if amino_acid == 'A':
		weight = weight + 71.03711
	elif amino_acid == 'C':
		weight = weight + 103.00919
	elif amino_acid == 'D':
		weight = weight + 115.02694
	elif amino_acid == 'E':
		weight = weight + 129.04259
	elif amino_acid == 'F':
		weight = weight + 147.06841
	elif amino_acid == 'G':
		weight = weight + 57.02146
	elif amino_acid == 'H':
		weight = weight + 137.05891
	elif amino_acid == 'I':
		weight = weight + 113.08406
	elif amino_acid == 'K':
		weight = weight + 128.09496
	elif amino_acid == 'L':
		weight = weight + 113.08406
	elif amino_acid == 'M':
		weight = weight + 131.04049
	elif amino_acid == 'N':
		weight = weight + 114.04293
	elif amino_acid == 'P':
		weight = weight + 97.05276
	elif amino_acid == 'Q':
		weight = weight + 128.05858
	elif amino_acid == 'R':
		weight = weight + 156.10111
	elif amino_acid == 'S':
		weight = weight + 87.03203
	elif amino_acid == 'T':
		weight = weight + 101.04768
	elif amino_acid == 'V':
		weight = weight + 99.06841
	elif amino_acid == 'W':
		weight = weight + 186.07931
	elif amino_acid == 'Y':
		weight = weight + 163.06333 
	a = a+1
	b = b+1

print weight
