#!/usr/bin/env python3
tmp = -1
a_n = []
while tmp != 0 :
    tmp = int(input())
    a_n.append(tmp)
a_n.reverse()
print(*a_n, sep="\n")