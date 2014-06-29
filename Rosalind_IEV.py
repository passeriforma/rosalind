#!/usr/bin/env python

# Given: Six positive integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes: AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa
# Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

f = open('input')
lines = f.read()
f.close()

couples = lines.split()

offspring = int(couples[0])*2 + int(couples[1])*2 + int(couples[2])*2 + int(couples[3])*(3/2.0) + int(couples[4])

print offspring
