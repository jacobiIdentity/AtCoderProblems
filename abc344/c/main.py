#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
m = int(input())
b_m = list(map(int,input().split()))
l = int(input())
c_l = list(map(int,input().split()))
q = int(input())
x_q = list(map(int,input().split()))
candidates = set()
for a in a_n :
    for b in b_m :
        for c in c_l :
            candidates.add(a+b+c)

for x in x_q :
    print("Yes" if x in candidates else "No")
    