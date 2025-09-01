#!/usr/bin/env python3
import itertools
s,k = input().split()
sSorted = sorted(list(s))
k = int(k)
print(''.join(sorted(list(set(itertools.permutations(sSorted, len(s)))))[k-1]))
