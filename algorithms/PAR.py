#!/usr/bin/env python

# Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.
# Return: A permuted array B[1..n] such that it is a permutation of A and there is an index 1≤q≤n such that B[i]≤A[1] for all 1≤i≤q−1, B[q]=A[1], and B[i]>A[1] for all q+1≤i≤n.

import sys

f = open('input')
lines = f.read().split('\n')
f.close()

n = int(lines[0])
arrayA = lines[1].split()
for x in range(0, n):
    arrayA[x] = int(arrayA[x])

pivot = arrayA[0]
arrayB = []
arrayB.append(pivot) 
positionPivot = 0

def addElement(pivot, element, array, positionPivot):
    if element > pivot:
        array.append(element)
        return array
    elif element < pivot:
        positionPivot += 1
        return [element] + array
    else: # Same value as the pivot
        left = array[:positionPivot]
        right = array[positionPivot:]
        return left + [pivot] + right

for element in arrayA[1:]:
    temp = addElement(pivot, element, arrayB, positionPivot)
    arrayB = temp

for element in arrayB:
    sys.stdout.write(str(element) + ' ')
print('')
