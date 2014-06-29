#!/usr/bin/env python

# Given: At most 15 UniProt Protein Database access IDs.
# Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

import re
import sys
import urllib2

f = open('input')
proteins = f.read()
proteins = proteins.split('\n')
f.close()

motif = 'N[^P][S|T][^P]'

for x in range(0, len(proteins)):
    proteinid = proteins[x]
    try:
        response = urllib2.urlopen('http://www.uniprot.org/uniprot/' + proteinid + '.fasta')
        html = response.read()
        fasta = re.sub('\n', '', html)
        fasta = fasta.split('SV=')[1]
        matches = []
        for i in range(0, len(fasta)-3):
           if re.search(motif, fasta[i:i+4]) != None:
               matches.append(i)
        if len(matches) != 0:
            print(proteinid)
            for match in matches:
               sys.stdout.write(str(match) + ' ')
            print('')
    except:
        sys.stdout.write('')
