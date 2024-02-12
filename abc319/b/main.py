#!/usr/bin/env python3
n = int(input())
ans = ""
for i in range(n+1) :
    for j in range(1,10) :
        if n%j != 0 :
            continue
        if i%(n//j) == 0 :
            ans += str(j)
            break
    if len(ans) != i+1 :
        ans += "-"
print(ans)