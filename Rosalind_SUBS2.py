#!/usr/bin/env python

f = open('input')
lines = f.read().split('\n')

string = lines[0]
subs = lines[1]

zstring = subs + ' ' + string

zvalues = []
zvalues.append(0) # first index has no substring match

l = 0 # Left position of current longest substring
r = 0 # Right position of current longest substring
k = 1

while k < len(zstring):
    if k > r: # Outside previous longest substring
        counter = 0 # For naive comparison to beginning of string
        zk = 0
        ktemp = k
        while ktemp < len(zstring) and zstring[ktemp] == zstring[counter]:
            ktemp += 1
            counter += 1
            zk += 1
        zvalues.append(zk)
        if zk > 0:
            r = k + zk - 1
            l = k
    else: # Inside current longest substring
        zkprime = zvalues[k-l] # Equivalent value in prefix
        beta = r-k
        if zkprime < beta: # Does not progress outside current longest substring
            zvalues.append(zvalues[zkprime])
            # r and l remain unchanged
        else: # New longest substring potentially present
            zk = r-k
            rightmatch = r
            leftmatch = beta
            while rightmatch < len(zstring) and zstring[rightmatch] == zstring[leftmatch]:
                zk += 1
                rightmatch += 1
                leftmatch += 1
            zvalues.append(rightmatch-k)
            r = rightmatch-1
            l = k
    k += 1

# Print out locations of substring matches
for i in range (len(subs)+1, len(zstring)):
    if zvalues[i] == len(subs):
        print(i-len(subs)),
