#!/usr/bin/env python3
n,k = map(int, input().split())
a_n = list(map(int, input().split()))
# cnt,tmp,i = 0,0,0
cnt,tmp = 0,0
# while i < n :
for i in range(n):
    if tmp+a_n[i] <= k :
        tmp += a_n[i]
    else :
        # print(i,a_n[i],k)
        cnt += 1
        tmp = a_n[i]
print(cnt+1)