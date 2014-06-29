#!/usr/bin/env python

# Given: A positive integer n <= 10^5 and an array A[1..n] of integers from -10^5 to 10^5.
# Return: The number of inversions in A.

f = open('input')
nums = f.read().split('\n')
f.close()

array_len = int(nums[0])
array = nums[1].split() 
for x in range(0, array_len):
    array[x] = int(array[x])

# Write a merge sort
# Then somehow magically count with it
