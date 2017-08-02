#!/usr/bin/env python

# Given: A positive integer n <= 10^5 and an array A[1..n] of integers from -10^5 to 10^5

# Return: An array B[1..n] such that it is a permutation of A and there are indices 
# 1 <= q <= r <= n such that B[i] < A[1] for all 1 <= i <= q-1, B[i] = A[1] for all
# q <= i <= r, and B[i]>A[1] for all r+1 <= i <= n.

import sys

# Read in inputs
inputs = sys.stdin.readlines()

length = int(inputs[0])
numbers = inputs[1][:-1].split(' ')

divider = int(numbers[0])

lesser = []
greater = []
equal = []

# Split numbers based on their size relative to the divider
for n in numbers:
    n = int(n)
    if n > divider:
        greater.append(n)
    elif n < divider:
        lesser.append(n)
    else:
        equal.append(n)

# Print the semi-sorted numbers
for num in lesser:
    sys.stdout.write(str(num) + " ")
for num in equal:
    sys.stdout.write(str(num) + " ")
for num in greater:
    sys.stdout.write(str(num) + " ")
sys.stdout.write("\n")
