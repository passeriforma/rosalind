#!/usr/bin/env python

# Given: A positive integer n≤25.
# Return: The value of Fn.

recursions = 21 
prev = 1
fib_number = 2

if recursions <= 2:
    print 1
else:
    recursions = recursions - 3 
    while recursions > 0:
        temp = fib_number
        fib_number = fib_number + prev
        prev = temp
        recursions = recursions - 1
    print fib_number
