#!/usr/bin/env python

# Given: Two positive integers n≤105 and m≤105, a sorted array A[1..n] of integers from −105 to 105 and a list of m integers −105≤k1,k2,…,km≤105.
# Return: For each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is no such index.

import sys

f = open("input")
file = f.read()
f.close()
file = file.split('\n')
n = file[0] # length of A
m = file[1] # length of listm
A = file[2]
A = A.split()
listm = file[3]
listm = listm.split()

for number in range(0, int(m)):
    x = int(listm[number])
    low = 0
    high = int(n)
    toprint = 0
    while low < high:
        mid = int((low+high)/2)
        midval = int(A[mid])
        if midval < x:
            low = mid+1
        elif midval > x:
            high = mid
        elif midval == x:
            toprint = mid+1
            break
    if int(toprint) == 0:
        sys.stdout.write("-1 ")
    else:
        sys.stdout.write(str(toprint) + ' ')

print('')
