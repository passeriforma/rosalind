#!/usr/bin/env python

# Given: A positive integer n≤7.
# Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

import itertools
import math
import re

length = 5
factorial_list = []
a = 1
input_value = length

while a < length+1:
	factorial_list.append(input_value)
	input_value = input_value -1
	a = a+1

permutations = [x for x in itertools.permutations(factorial_list)]

end_char = 3*length -1

print math.factorial(length)

for group in permutations:
	print group

