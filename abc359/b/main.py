#!/usr/bin/env python3
n = int(input())
a_2n = list(map(int,input().split()))
ans = 0
for i in range(2*n) :
    if i > 1 and a_2n[i] == a_2n[i-2] :
        ans += 1
print(ans)