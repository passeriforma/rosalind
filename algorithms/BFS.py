#!/usr/bin/env python

# Given: A simple directed graph with n≤103 vertices in the edge list format.
# Return: An array D[1..n] where D[i] is the length of a shortest path from the vertex 1 to the vertex i (D[1]=0). If i is not reachable from 1 set D[i] to −1.

import sys

f = open('input')
cons = f.read()
f.close()
cons = cons.split('\n')

vertices = int(cons[0].split()[0])
edges = int(cons[0].split()[1])

# Place vertices into graph representation
graph = {}
for i in range(1, vertices+1):
    graph[i] = []

for x in range(1, edges+1):
    start = int(cons[x].split()[0])
    end = int(cons[x].split()[1])
    graph[start].append(end)

# Perform a bfs
distance = {}
for i in range(1, vertices+1):
    distance[i] = 0

queue = []
for connecting in range(0, len(graph[1])):
    node = graph[1][connecting]
    distance[node] = 1
    queue.append(node)

while queue:
    vertex = queue.pop(0)
    for connection in range(0, len(graph[vertex])):
        node = int(graph[vertex][connection])
        if distance[node] == 0 and node != 1: # Node has not been calculated
            distance[node] = distance[vertex] + 1
            queue.append(node)

sys.stdout.write(str(distance[1]) + ' ')
for vertice in range(2, vertices + 1):
    if distance[vertice] != 0:
        sys.stdout.write(str(distance[vertice]) + ' ')
    else:
        sys.stdout.write('-1 ')
print('')
