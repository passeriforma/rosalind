#!/usr/bin/env python

# Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.
# Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.

from sympy import binomial

f = open('input')
lines = f.read().split()
f.close()
k = int(lines[0])
N = int(lines[1])

# Sum of all probabilities that are not Aa Bb = 0
# So, 1 - (P(0) + P(1) + P(2) + P(3) + ... + P(N))

probabilities = []

def P(n, k):
    # Bernoulli trial (ew)
    return binomial(2**k, n) * 0.25**n * 0.75**(2**k - n)

print 1 - sum([P(n, k) for n in range(N)])
