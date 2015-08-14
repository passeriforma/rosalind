#!/usr/bin/env python

# Given: Positive integers n≤100 and m≤20.
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

f = open('input')
nums = f.read().split()
f.close()

months = int(nums[0])
ageofdeath = int(nums[1])
currentRabbits = 1
currentMonth = 1
rabbits = []

for i in range(months):
	if i < ageofdeath:
		if i == 0 or i == 1:
			rabbits.append(1)
		else:
			rabbits.append(rabbits[-1] + rabbits[-2])
	else:
		rabbit = 0
		for c in range(i-ageofdeath, i-1): #ignore all dead
			rabbit = rabbit + rabbits[c]
		rabbits.append(rabbit)

print rabbits[months-1]
