#!/usr/bin/env python3
a_63 = list(map(int,input().split()))
ans = 0
for i in reversed(range(64)) :
    ans <<= 1
    ans += a_63[i]
print(ans)