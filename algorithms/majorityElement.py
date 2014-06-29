#!/usr/bin/env python

# Given: A positive integer k≤20, a positive integer n≤104, and k arrays of size n containing positive integers not exceeding 105.
# Return: For each array, output an element of this array occurring strictly more than n/2 times if such element exists, and "-1" otherwise.

import sys

f = open("input")
file = f.read()
f.close
file = file.split('\n')

numbers = file[0]
numbers = numbers.split(' ')
k = int(numbers[0]) # number of arrays
n = int(numbers[1]) # size of arrays

for array in range(1, k+1):
    letters = {}
    string = file[array]
    string = string.split()
    for letter in string:
        if letter in letters.keys():
            letters[letter] = letters[letter] + 1
        else:
            letters[letter] = 1
    toprint = -1
    for key, value in letters.iteritems():
        if value > (n/2):
            toprint = key
    sys.stdout.write(str(toprint) + ' ')
