#!/usr/bin/env python

# Given: A positive integer n <= 10^5 and an array A[1..n] of integers from -10^5 to 10^5.

# Return: A sorted array A[1..n].

import sys

f = open('input')
lines = f.read()
f.close()

lines = lines.split('\n')

length = int(lines[0])

array = lines[1]
array = array.split()
for x in range(0, length):
    value = int(array[x])
    array[x] = value

def merge_sort(seq):
    if len(seq) == 1:
        return seq
    else:
        mid = len(seq)/2
        left = merge_sort(seq[:mid])
        right = merge_sort(seq[mid:])

        i, j, k = 0, 0, 0 #i= left counter, j= right counter, k= master counter

        while i < len(left) and j < len(right):
            #if current left val is < current right val; assign to master list
            if left[i] < right[j]:
                seq[k] = left[i]
                i += 1; k += 1
            #else assign right to master
            else:
                seq[k] = right[j]
                j += 1; k += 1

        #handle remaining items in remaining list
        remaining = left if i < j else right
        r = i if remaining == left else j

        while r < len(remaining):
            seq[k] = remaining[r]
            r += 1; k += 1

        return seq

array = merge_sort(array)

for a in range(0, length):
    sys.stdout.write(str(array[a]) + ' ')
print ''
