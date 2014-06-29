#!/usr/bin/env python

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

f = open('rosalind_gc.txt')
current = ''
gc_current = 0
total_strand = 0
max_gc = 0
max_gc_title = ''

for line in f:
    if line[0] == '>':
        percentage = (gc_current/float(total_strand-1))*100
        if percentage > max_gc:
            max_gc = percentage
            max_gc_title = current
        gc_current = 0
        total_strand = 0
        current = line
    else:
        for char in line:
            if char == 'C' or char == 'G':
                gc_current = gc_current + 1
            total_strand = total_strand + 1

f.close

print max_gc_title
print max_gc
