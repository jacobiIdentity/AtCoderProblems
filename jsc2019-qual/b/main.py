#!/usr/bin/env python3
n,k = map(int,input().split())
a_n = list(map(int,input().split()))
a1 = [0]*n
a2 = [0]*n
for i in range(n) :
    for j in range(n) :
        if a_n[i] > a_n[j] :
            a2[i] += 1
            if i < j :
                a1[i] += 1
# print(a_n)
# print(a1)
# print(a2)
div = 10**9+7
ans = sum([(k*a1[i]+a2[i]*(k*(k-1))//2)%div for i in range(n)])
print(ans%div)