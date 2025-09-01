#!/usr/bin/env python3
n = int(input())
s = 'A'+input()
ans = 0
for i in range(1,n) :
    l = n-i
    for k in range(1,n-i+1) :
        if s[k]==s[k+i] :
            l = k-1
            break
    print(l)