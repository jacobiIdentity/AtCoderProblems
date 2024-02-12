#!/usr/bin/env python3
n, m = map(int, input().split())
c_n = input().split()
d_m = input().split()
p_m1 = list(map(int, input().split()))
ans = 0
for i in range(n) :
    if c_n[i] in d_m :
        ans += p_m1[d_m.index(c_n[i])+1]
    else :
        ans += p_m1[0]
print(ans)