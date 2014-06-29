#!/usr/bin/env python

# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s.

import sys

dna = sys.stdin.read()
#print dna

#slice dna[a:b] a=0, b=3 then add three every time to both until string end

a=0
b=3

while dna[b] != '\n':
	codon = dna[a:b]
#	print codon
	if codon == 'UUU' or codon == 'UUC':
		sys.stdout.write('F')
	elif codon == 'UUA' or codon == 'UUG' or codon == 'CUU' or codon == 'CUC' or codon == 'CUA' or codon == 'CUG':
		sys.stdout.write('L')
	elif codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG' or codon == 'AGU' or codon == 'AGC':
		sys.stdout.write('S')
	elif codon == 'UAU' or codon == 'UAC':
		sys.stdout.write('Y')
	elif codon == 'UGU' or codon == 'UGC':
		sys.stdout.write('C')
	elif codon == 'UGG':
		sys.stdout.write('W')	
	elif codon == 'CUU' or codon == 'CUC' or codon == 'CUA' or codon == 'CUG':
		sys.stdout.write('L')
	elif codon == 'CCU' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG':
		sys.stdout.write('P')
	elif codon == 'CAU' or codon == 'CAC':
		sys.stdout.write('H')
	elif codon == 'CAA' or codon == 'CAG':
		sys.stdout.write('Q')
	elif codon == 'CGU' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
		sys.stdout.write('R')
	elif codon == 'AUU' or codon == 'AUC' or codon == 'AUA':
		sys.stdout.write('I')
	elif codon == 'AUG':
		sys.stdout.write('M')
	elif codon == 'ACU' or codon == 'ACC' or codon == 'ACG' or codon == 'ACA':
		sys.stdout.write('T')
	elif codon == 'AAU' or codon == 'AAC':
		sys.stdout.write('N')
	elif codon == 'AAA' or codon == 'AAG':
		sys.stdout.write('K')
	elif codon == 'GUU' or codon == 'GUC' or codon == 'GUA' or codon == 'GUG':
		sys.stdout.write('V')
	elif codon == 'GCU' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
		sys.stdout.write('A')
	elif codon == 'GAU' or codon == 'GAC':
		sys.stdout.write('D')
	elif codon == 'GAA' or codon == 'GAG':
		sys.stdout.write('E')
	elif codon == 'GGU' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
		sys.stdout.write('G')
	elif codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
		pass
	else:
		print "Well thats a fuckup"
	a = a+3
	b = b+3

print ''
