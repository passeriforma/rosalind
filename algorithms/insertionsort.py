#!/usr/bin/env python

# Given: A positive integer n≤103 and an array A[1..n] of integers.
# Return: The number of swaps performed by insertion sort algorithm on A[1..n].

f = open("input")
inputs = f.read()
inputs = inputs.split('\n')
n = inputs[0] #length of array
array = inputs[1]
array = array.split()
print array
outputarray = [None]*(int(n))
swaps = 0

for j in range(1, int(n)):
    key = int(array[j])
    i = j - 1
    while i > -1 and int(array[i]) > key:
        array[i+1] = array[i]
        i = i - 1
        swaps += 1
    array[i+1] = key

print array
print swaps
