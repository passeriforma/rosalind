#!/usr/bin/env python

# Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.
# Return: The total number of partial permutations P(n,k), modulo 1,000,000.

import math

f = open('input')
nums = f.read().split()
f.close()

n = int(nums[0])
k = int(nums[1])

numerator = math.factorial(n)
denominator = math.factorial(n-k)
value = (numerator/denominator)%1000000
print value
