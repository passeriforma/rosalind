#!/usr/bin/env python

# Given: A simple graph with n≤103 vertices in the edge list format.
# Return: An array D[1..n] where D[i] is the degree of vertex i.

import sys

f = open('input')
graph = f.read()
f.close()

graph = graph.split('\n')
vertices = int(graph[0].split()[0])
edges = int(graph[0].split()[1])

numconnections = {}
for a in range(1, vertices+1):
    numconnections[a] = 0

for x in range(1, edges+1):
    connection = graph[x].split()
    start = int(connection[0])
    end = int(connection[1])
    numconnections[start] += 1
    numconnections[end] += 1

for i in range(1, vertices+1):
    sys.stdout.write(str(numconnections[i]) + ' ')
print ''
