#!/usr/bin/env python

# Given: A positive integer n≤105 and a sorted array A[1..n] of integers from −105 to 105, a positive integer m≤105 and a sorted array B[1..m] of integers from −105 to 105.
# Return: A sorted array C[1..n+m] containing all the elements of A and B.

f = open('input')
contents = f.read()
f.close()

contents = contents.split('\n')
n = int(contents[0]) #lenA
m = int(contents[2]) #lenB
A = contents[1].split()
B = contents[3].split()

C = []

pointerA = 0
pointerB = 0

for x in range(0, (m+n)):
    if pointerA == n:
        C.append(B[pointerB])
        pointerB += 1
    elif pointerB == m:
        C.append(A[pointerA])
        pointerA += 1
    elif int(A[pointerA]) > int(B[pointerB]):
        C.append(B[pointerB])
        pointerB += 1
    elif int(A[pointerA]) <= int(B[pointerB]):
        C.append(A[pointerA])
        pointerA += 1

print ' '.join(C)
