#!/usr/bin/env python3
k,s = map(int,input().split())
ans = 0
tgt = set()
if s%3==0 and s//3 <= k : ans += 1
for a in range(k+1) :
    if 0 <= s-2*a <= k and a != s-2*a :
        ans += 3
for a in range(k+1) :
    for b in range(a+1,k+1) :
        if b<s-a-b <= k :
            ans += 6
print(ans)
# print(tgt)