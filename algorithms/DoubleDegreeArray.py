#!/usr/bin/env python

# Given: A simple graph with n≤103 vertices in the edge list format.
# Return: An array D[1..n] where D[i] is the sum of the degrees of i's neighbors.

import sys

f = open('input')
inputs = f.read()
f.close()

inputs = inputs.split('\n')
vertices = int(inputs[0].split()[0])
edges = int(inputs[0].split()[1])

numconnections = {}
links = {}

for i in range(1, vertices+1):
    numconnections[i] = 0
    links[i] = []

for x in range(1, edges+1):
    start = int(inputs[x].split()[0])
    end = int(inputs[x].split()[1])
    numconnections[start] += 1
    numconnections[end] += 1
    links[start].append(end)
    links[end].append(start)

for a in range(1, vertices+1):
    degree = 0
    for num in links[a]:
        degree = degree + numconnections[num]
    sys.stdout.write(str(degree) + ' ')
print ''
