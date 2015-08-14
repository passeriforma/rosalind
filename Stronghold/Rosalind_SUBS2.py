#!/usr/bin/env python

f = open('input')
lines = f.read().split('\n')

string = lines[1] # Note that this is substring first, string second
subs = lines[0]

zstring = subs + ' ' + string

zvalues = []
zvalues.append(0) # first index has no substring match

l = 0 # Left position of current longest substring
r = 0 # Right position of current longest substring
k = 1

while k < len(zstring):
    if k > r: # Outside previous longest substring
#        print(1, l, r),
        counter = 0 # For naive comparison to beginning of string
        zk = 0
        ktemp = k
        while ktemp < len(zstring) and zstring[ktemp] == zstring[counter]:
            ktemp += 1
            counter += 1
            zk += 1
        zvalues.append(zk)
        if zk > 0:
            r = k + zk
            l = k
    else: # Inside current longest substring
        zkprime = zvalues[k-l] # Equivalent value in prefix
        beta = r-k
        if zkprime < beta: # Does not progress outside current longest substring
#            print(2, l, r),
            zvalues.append(zvalues[zkprime])
            # r and l remain unchanged
        else: # New longest substring potentially present
#            print(3, l, r),
            zk = r-k
            rightmatch = r
            leftmatch = beta
            while rightmatch < len(zstring) and zstring[rightmatch] == zstring[leftmatch]:
                zk += 1
                rightmatch += 1
                leftmatch += 1
            zvalues.append(rightmatch-k)
            r = rightmatch
            l = k
    k += 1
# Print out locations of substring matches
for i in range (len(subs)+1, len(zstring)):
    if zvalues[i] == len(subs):
        print(i-len(subs)-1),

