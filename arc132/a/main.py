#!/usr/bin/env python3
n = int(input())
r_n = list(map(int,input().split()))
c_n = list(map(int,input().split()))
q = int(input())
ans = ''
for _ in range(q) :
    r,c = map(int,input().split())
    ans += '#' if n- r_n[r-1]+1 <= c_n[c-1] else '.'
print(ans)
