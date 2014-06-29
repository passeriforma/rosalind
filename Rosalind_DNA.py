#!/usr/bin/env python

# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

def countNucleotides(string):
    a = 0
    c = 0
    g = 0
    t = 0
    for letter in string:
        if letter == 'A':
            a = a + 1
        if letter == 'C':
            c = c + 1
        if letter == 'G':
            g = g+1
        if letter == 'T':
            t = t+1
    print(str(a) + ' ' + str(c) + ' ' + str(g) + ' ' + str(t))

f = open("input")
lines =  f.read()
lines = lines.strip('\n')
countNucleotides(lines)
