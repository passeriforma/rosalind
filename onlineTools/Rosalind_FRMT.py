#!/usr/bin/env python

# Given: A collection of n (n≤10) GenBank entry IDs.
# Return: The shortest of the strings associated with the IDs in FASTA format.

import sys
from Bio import Entrez
from Bio import SeqIO

Entrez.email = 'emsaundwalm@gmail.com'

handle = Entrez.efetch(db="nucleotide", id=["JX317645, JX569368, NM_214399, JX295575, NM_001168970, NM_001133698, NM_002124, JX491654, JQ867090, NM_001246828"], rettype="fasta")
record = list (SeqIO.parse(handle, "fasta")) #get list of seqIO objects in FASTA format

shortest = 0
length = 0

for x in range(0, len(record)):
    rec = record[x].seq
    lengthC = len(rec)
    if x == 0:
        length = lengthC
    else:
        if lengthC < length:
            shortest = x
            length = lengthC
        print x

print record[shortest].description  #description, sequence
print record[shortest].seq
