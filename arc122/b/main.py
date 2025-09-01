#!/usr/bin/env python3
n = int(input())
a_n = sorted(list(map(int,input().split())))
sumA = sum(a_n)
ans = min(2*sumA - n*a_n[0],2*n*a_n[-1])
for i in range(1,n) :
    sumA -= a_n[i-1]
    ans = min(ans,2*sumA-(n-2*i)*a_n[i])

print(ans/(2*n))