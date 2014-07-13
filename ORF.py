#!/usr/bin/env python

f = open('input')
DNA = f.read()
f.close()

def identifyORFs(DNA):
    start_codon = 'ATG'
    end_codons = ['TAA', 'TAG', 'TGA']

    # Gives the reverse compliment of a string
    def reverseCompliment(DNA):
        reverse = {
        'A': 'T', 'T':'A', 'C':'G', 'G':'C', '\n':'\n'
        }
        strand = []
        for codon in DNA:
            strand.append(reverse[codon])
        return ''.join(reversed(strand))

    # Gives the DNA of each ORF frame in the input DNA string
    def findORFs(DNA, frames):
        for x in range(0, len(DNA), 3):
            inORF = False
            codon = DNA[x:x+3]
            if codon == start_codon:
                substring = DNA[x:]
                end_location = []
                for end in end_codons:
                    end_location.append(substring.find(end))
                # TODO: find minimum (not-1) value in string
                frames.append(DNA[x:x+ending])
        return frames

    frames = []
    frames.append(findORFs(DNA, frames))
    frames.append(findORFs(reverseCompliment(DNA), frames))
    return frames

print(identifyORFs(DNA)) 
