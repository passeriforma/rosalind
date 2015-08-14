#!/usr/bin/env python

# Given: A positive integer n≤6.
# Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).

import itertools
import math
import re

length = 3

total = (2**length)*math.factorial(length)
print total

c = 0
input_value = length
choices = []
sum_of_elements = 0

#put positives and negatives in an array
while c < (2*length+1):
	choices.append(input_value)
	c = c+1
	if input_value > 0:
		sum_of_elements = sum_of_elements + input_value
	else:
		pass
	input_value = input_value -1

#print choices
#print sum_of_elements

#remove 0
del choices[length]

#from 2*length, make all the permutations
permutations = list(itertools.permutations(choices, length))

#remove ones with + and - of the same number
n=0
group_sum = 0
for groups in permutations:
	while n < length:
		addition = abs(groups[n])
		#print addition
		group_sum = group_sum + addition
		n = n+1
	if group_sum == sum_of_elements:
		print groups
	else:
		del groups
	n=0
	group_sum = 0	
