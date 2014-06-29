#!/usr/bin/env python

# Given: A genus name, followed by two dates in YYYY/M/D format.
# Return: The number of Nucleotide GenBank entries for the given genus that were published between the dates specified.

from Bio import Entrez

term = "Nesterenkonia"
start = "2001/03/24"
end = "2011/09/19"

Entrez.email = 'emsaundwalm@gmail.com'
handle = Entrez.esearch(db="nucleotide", term='"' + term + '"[Organism] AND ("' + start + '"[PDAT] : "' + end + '"[PDAT])"')
record = Entrez.read(handle)
print record["Count"]
