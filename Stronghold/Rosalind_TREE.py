#!/usr/bin/env python

# Given: A positive integer n (n≤1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.
# Return: The minimum number of edges that can be added to the graph to produce a tree.

f = open('input')
lines = f.read()
lines = lines.split('\n')
lines.pop()
nodes = int(lines[0])

# Sneaky hack
edges = len(lines)
print nodes - edges
