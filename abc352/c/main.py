#!/usr/bin/env python3
n = int(input())
a_n = []
b_n = []
for _ in range(n) :
    a,b = map(int,input().split())
    a_n.append(a)
    b_n.append(b)
tmp = sum(a_n)
ans = tmp - a_n[0]+ b_n[0]
for i in range(n) :
    topI = tmp- a_n[i]+ b_n[i]
    ans = topI if topI >= ans else ans
print(ans)
