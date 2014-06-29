#!/usr/bin/env python

# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

months = 30
babyPairs = 3
pastR = 1
rabbits = 1
start = 2 

if months > 2:
	while start < months:
		start = start + 1
		temp = rabbits
		rabbits = rabbits + pastR*babyPairs
		pastR = temp
		print rabbits		

print rabbits
