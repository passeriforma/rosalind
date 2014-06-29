#!/usr/bin/env python

# Given: The UniProt ID of a protein.
# Return: A list of biological processes in which the protein is involved (biological processes are found in a subsection of the protein's "Gene Ontology" (GO) section).

# Requires one uniprot protein ID as a commandline argument

import sys
import urllib2

if len(sys.argv) != 2:
    print("Wrong number of arguments. Expecting one uniprot protein ID.")
else:
    protein = sys.argv[1]
    page = urllib2.urlopen('http://www.uniprot.org/uniprot/' + protein)
    page = page.read()
    page = page.split('Biological_process')[1]
    page = page.split('Molecular_function')[0]
    page = page.split('Cellular_component')[0]
    page = page.split("'Display-GO-Term');")
    x = 1
    while x < len(page):
        section = page[x]
        section = section[2:]
        section = section.split('<')[0]
        print section
        x = x + 1
