#!/usr/bin/env python3
s_n = list(map(int, input().split()))
ans = 'Yes'
tmp = 0
for i in range(8) :
    tmp = s_n[i-1] if i != 0 else s_n[i]
    if i != 0 and tmp > s_n[i] :
        ans = 'No'
    if s_n[i] < 100 or s_n[i] > 675 :
        ans = 'No'
    if s_n[i]%25 != 0 :
        ans = 'No'
print(ans)


