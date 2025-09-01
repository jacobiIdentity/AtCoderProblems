#!/usr/bin/env python3
n = int(input())
a_ij = [list(input()) for _ in range(n)]
b_ij = [row[:] for row in a_ij]  # Shallow copy of the matrix

# Rotate the matrix
for i in range(n):
    for j in range(n):
        b_ij[j][n + 1 - i] = a_ij[i][j]

# Print the rotated matrix
for row in b_ij:
    print(''.join(row))
