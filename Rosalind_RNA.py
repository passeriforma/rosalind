#!/usr/bin/env python

# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.

import sys
import string

dna = sys.stdin.read()

rna = dna.replace('T', 'U')

print rna
