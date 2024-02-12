#!/usr/bin/env python3
n = int(input())
d_n = list(map(int,input().split()))
ans = 0
for i in range(n) :
    month = str(i+1)
    for j in range(d_n[i]) :
        day = str(j+1)
        if len(set(list(month+day))) == 1 :
            ans += 1
print(ans)
