#!/usr/bin/env python3
h,w,d = map(int,input().split())
grid = [input() for _ in range(h)]
ans = 2
for i in range(h) :
    for j in range(w) :
        if grid[i][j] == '#' :
            continue
        for k in range(h) :
            for l in range(w) :
                if i==k and j==l :
                    continue
                if grid[k][l] == '#' :
                    continue
                tmp = 0
                for m in range(h) :
                    for n in range(w) :
                        if grid[m][n] == '.' and \
                           (abs(m-i)+abs(n-j) <= d or abs(m-k)+abs(n-l) <= d ) :
                            tmp += 1
                ans = max(tmp,ans)
print(ans)