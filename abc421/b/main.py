#!/usr/bin/env python3
def calc(a1,a2) :
    return int("".join(reversed(list(str(a1+a2)))) )
a_n = list(map(int,input().split()))
for _ in range(10) :
    a_n.append(calc(a_n[-1],a_n[-2]))
print(a_n[9])