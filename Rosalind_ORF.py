#!/usr/bin/env python

# Given: A DNA string s of length at most 1 kbp in FASTA format.
# Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

dna_codons = {
'TTT': 'F',      'CTT': 'L',      'ATT': 'I',      'GTT': 'V',
'TTC': 'F',      'CTC': 'L',      'ATC': 'I',      'GTC': 'V',
'TTA': 'L',      'CTA': 'L',      'ATA': 'I',      'GTA': 'V',
'TTG': 'L',      'CTG': 'L',      'ATG': 'M',      'GTG': 'V',
'TCT': 'S',      'CCT': 'P',      'ACT': 'T',      'GCT': 'A',
'TCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
'TCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
'TCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
'TAT': 'Y',      'CAT': 'H',      'AAT': 'N',      'GAT': 'D',
'TAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
'TAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
'TAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
'TGT': 'C',      'CGT': 'R',      'AGT': 'S',      'GGT': 'G',
'TGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
'TGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
'TGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G',
}

start_codon = 'ATG'
end_codons = ['TAA', 'TAG', 'TGA']

def reverse_complement(strand):
    comp = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
        '\n':'\n',
        }
    return ''.join(comp[b] for b in reversed(strand))

def all_indices(s, sub):
    i = s.find(sub)
    while i != -1:
        yield i
        i = s.find(sub, i+1)

def end_codon_index(s, start=0):
    end_indices = []
    for codon in end_codons:
        end = s.find(codon, start)
        while True:
            if end == -1:
                break
            elif (end - start) % 3 == 0:
                end_indices.append(end)
                break
            else:
                end = s.find(codon, end + 1)
    return min(end_indices) if end_indices else None

def open_reading_frame(s, start):
    end = end_codon_index(s, start)
    if end:
        return s[start:end_codon_index(s, start)]
    return ''

def translate_dna(dna):
    protein = ''
    for i in xrange(0, len(dna), 3):
        protein += dna_codons[dna[i:i+3]]
    return protein

def all_open_reading_frames(s):
    r = ''.join(reverse_complement(s))
    return set([translate_dna(open_reading_frame(s, start))
                for start
                in all_indices(s, start_codon)]
               +
               [translate_dna(open_reading_frame(r, start))
                for start
                in all_indices(r, start_codon)]) ^ set([''])


if __name__ == '__main__':
    import sys

    strand = open('input').read()
    strand = strand.strip('\n')
    print '\n'.join(all_open_reading_frames(strand))
