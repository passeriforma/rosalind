#!/usr/bin/env python

# Given: A collection of n (n≤10) DNA strings.
# Return: The number of given strings that match their reverse complements.

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import re

f = open('input')
lines = f.read()
f.close()

lines = lines.split('>')

reverse_compliments = 0

for line in lines:
    dna = re.sub('[^GCAT]', '', line)
    dna = Seq(dna, IUPAC.unambiguous_dna)
    dnacompliment = dna.reverse_complement()
    if str(dna) == str(dnacompliment):
        reverse_compliments += 1

print reverse_compliments - 1
