#!/usr/bin/env python3
d = [0, 3, 1, 4, 1, 5, 9]
p, q = input().split()
op, oq = ord(p)-ord('A'), ord(q)-ord('A')
if op > oq :
    op, oq = oq, op
print(sum(d[op+1:oq+1]))
