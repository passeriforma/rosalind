#!/usr/bin/env python

# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

from math import factorial

k = float(19) #DD
m = float(30) #Dd
n = float(15) #dd
t = k+m+n

pk = k/t
pm = m/t
pn = n/t

totalProb = 1
#minus both parents recessive
totalProb = totalProb - pn*((n-1)/(t-1))
#minus one parent homozygous recessive and other heterozygous recessive (.5)
totalProb = totalProb - pn*(m/(t-1))
#minus probability of both heterozygous with recessive (.25)
totalProb =  totalProb - pm*((m-1)/(t-1))*0.25

print totalProb
