#!/usr/bin/env python3
k = int(input())
ans = 0
for a in range(1,k+1) :
    for b in range(1,k+1) :
        for c in range(1,k+1) :
            if a*b*c > k :
                break
            ans += 1
        if a*b > k :
            break
print(ans)