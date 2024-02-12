#!/usr/bin/env python3
n, x = map(int, input().split())
a_n = []
b_n = []
for _ in range(n) :
    a, b = map(int, input().split())
    a_n.append(a)
    b_n.append(b)
ans = a_n[0]+b_n[0]*x
sumAB = a_n[0]+b_n[0]
minB = b_n[0]
for i in range(min(n-1,x-1)) :
    # print(ans)
    minB = min(minB, b_n[i+1])
    sumAB += a_n[i+1]+b_n[i+1]
    # print(minB, sumAB, sumAB+minB*(x-i-1))
    ans = min(sumAB+minB*(x-i-2),ans)
print(ans)