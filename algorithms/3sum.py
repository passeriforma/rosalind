#!/usr/bin/env python

# Given: A positive integer k <= 20, a postive integer n <= 10^4, and k arrays of size n containing integers from -10^5 to 10^5.
# Return: For each array A[1..n], output three different indices 1 <= p < q < r <= n such that A[p]+A[q]+A[r]=0 if exist, and "-1" otherwise.

f = open('input')
files = f.read()
files = files.split('\n')
files0 = files[0].split()

k = int(files0[0]) #number of arrays
n = int(files0[1]) #array length


for x in range(1, k+1):
    found = False
    line = files[x]
    line = line.split()

    # Make hash table with all numbers in the thing
    numbers = {}
    for i in range(0, n):
        numbers[int(line[i])] = i

    for a in range(0, n):
        if found == True:
            break
        else:
            first = int(line[a])
        for b in range(a+1, n):
            second = int(line[b])
            if ((-1)*(first+second)) in numbers:
                c = numbers[(-1)*(first+second)]
                print(str(a+1) + ' ' + str(b+1) + ' ' + str(c+1))
                found = True
                break 
    if found == False:
        print '-1'

