#!/usr/bin/env python3
n = list(input())
h_n = list(enumerate(list(map(int, input().split()))))
h_n.sort(key=lambda x:x[1])
print(h_n[-1][0]+1)