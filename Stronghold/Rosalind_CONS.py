#!/usr/bin/env python

# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

f = open('rosalind_cons.txt', 'r')
strings = []
for DNA in f.readlines():
	strings.append(DNA.rstrip()) 
f.close()

DNAlength = len(strings[1])
profileA = []
profileC = []
profileG = []
profileT = []



for x in range(0, DNAlength):
	profileA.append(0)
	profileC.append(0)
	profileG.append(0)
	profileT.append(0)

n = 1
while n <= len(strings):
	string = strings[n]
	letters = list(string)
	c = 0
	while c < len(string):
		char = letters[c]
		if char == 'A':
			profileA[c] = profileA[c] + 1
		if char == 'C':
			profileC[c] = profileC[c] + 1
		if char == 'G':
			profileG[c] = profileG[c] + 1
		if char == 'T':
			profileT[c] = profileT[c] + 1
		c = c+1
	n = n+2  

consensus = []
for char in range(0, len(profileA)):
	d = {profileA[char]:'A', profileC[char]:'C', profileG[char]:'G', profileT[char]:'T'}
	maximum = max(k for k, v in d.iteritems())
	consensus.append(d[maximum])

print ''.join(consensus)

strA ='A: ' + ' '.join(str(e) for e in profileA)
strC ='C: ' + ' '.join(str(e) for e in profileC)
strG ='G: ' + ' '.join(str(e) for e in profileG)
strT ='T: ' + ' '.join(str(e) for e in profileT)
print strA.strip() + '\n' + strC.strip() + '\n' + strG.strip() + '\n' + strT.strip() 
