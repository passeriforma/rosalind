#!/usr/bin/env python

# Given: A positive integer n (3<=n<=10000)
# Return: The number of internal nodes of any unrooted binary tree having n leaves.

# In an unrooted binary tree with n leaves, there will be n-2 internal nodes. 

f = open('rosalind_inod.txt', 'r')
nodes = int(f.readline())
print nodes-2
