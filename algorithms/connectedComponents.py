#!/usr/bin/env python

# Given: A simple graph with n<=10^3 vertices in the edge list format.
# Return: The number of connected components in the graph.

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
    graph[end].append(start)

# Set up an array to check if each vertex has been covered or not
covered = [1]
for i in range(0, vertices):
    covered.append(0)

subgraphs = 0

# Perform BFS
while 0 in covered: #still unchecked nodes
    subgraphs += 1
    start = covered.index(0)

    covered[start] = 1

    queue = []
    if len(graph[start]) == 0: # No connections to other nodes
        continue
    else:
        for connecting in range(0, len(graph[start])):
            node = graph[start][connecting]
            covered[node] = 1
            queue.append(node)

        while queue:
            vertex = queue.pop(0)
            for connection in range(0, len(graph[vertex])):
                node = int(graph[vertex][connection])
                if covered[node] == 0 and node != start: # Node has not been calculated
                    covered[node] = 1
                    queue.append(node)

print subgraphs
