#!/usr/bin/env python

# Return the string that is the most different to the others. 

f = open('input')
lines = f.read().split('\n')
f.close()

dashes = []
for i in range(0, len(lines)):
    dashes.append(0)
    for char in lines[i]:
        if char == '-':
             dashes[i] += 1
    print(lines[i][0:15] + str(dashes[i]))
