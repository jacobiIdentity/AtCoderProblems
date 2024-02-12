#!/usr/bin/env python3
n , d  = map(int, input().split())
dots = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n) :
    for j in range(i+1,n) :
        l = 0
        for dd in range(d) :
            l += (dots[i][dd]-dots[j][dd])**2
        tmp = 1
        while tmp*tmp <= l :
            if tmp*tmp == l :
                ans += 1
                # print(i,j,l)
                break
            tmp += 1
print(ans)
