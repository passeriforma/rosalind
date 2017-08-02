#!/usr/bin/env python

# Given: A collection of n (n<=10) DNA strings of equal length (not exceeding 1 kbp). Strings are given in FASTA format.
# Return: The matrix D corresponding to the p-distance dsubp on the given strings. As always, note that your answer is allowed an absolute error of 0.001.

import sys

def main():
    inputs = sys.stdin.read()

    input_dna = []


    inputs = inputs.split('>')[1:]
    for seq in inputs:
        seq = seq.split('\n')[1:]
        seq = ''.join(seq)
        input_dna.append(seq)

    # Length is consistent, so just pick the first one
    length = len(input_dna[0])

    # Initialise a 2D array to store the Hamming Distances
    hamming_dist = []

    for i in range(0, len(input_dna)):
        hamming_dist.append([])
        strand_one = input_dna[i]
        for j in range(0, len(input_dna)):
            strand_two = input_dna[j]
            dist = 0 
            # if i == j, theyre the same string so don't need to be compared
            if i != j:
                dist = calculate_hamming_distance(strand_one, strand_two, length)
            hamming_dist[i].append(dist)

    p_dist = hamming_dist_to_pdist(hamming_dist, length)

    pretty_print(p_dist)

def pretty_print(array):
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            sys.stdout.write(("%.5f" % array[i][j]) + ' ')
        sys.stdout.write("\n")


def hamming_dist_to_pdist(hamming_dist, length):
    for i in range(0, len(hamming_dist)):
        for j in range(0, len(hamming_dist)):
            # P-distance is hamming distance divided by the DNA strand length
            hamming_dist[i][j] = (hamming_dist[i][j])/float(length)

    return hamming_dist

# Calculates the Hamming Distance between two DNA strands
def calculate_hamming_distance(strand_one, strand_two, length):
    a = 0
    hamming_distance = 0

    while a < length:
        if strand_one[a] == strand_two[a]:
            pass
        else:
            hamming_distance = hamming_distance + 1
        a = a+1

    return hamming_distance


if __name__ == "__main__":
    main()
