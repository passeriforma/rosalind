#!/usr/bin/env python

# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

def countNucleotides(string):
    a = c = g = t = 0
    for letter in string:
        if letter == 'A':
            a += 1
        if letter == 'C':
            c += 1
        if letter == 'G':
            g += 1
        if letter == 'T':
            t += 1
    print(str(a) + ' ' + str(c) + ' ' + str(g) + ' ' + str(t))

f = open("input")
lines =  f.read()
lines = lines.strip('\n')
countNucleotides(lines)
