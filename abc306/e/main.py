#!/usr/bin/env python3
from collections import defaultdict
n, k ,q = map(int, input().split())
x_y = [list(map(int, input().split())) for _ in range(q)]
d = defaultdict(int)
topK = [False]*n
cnt, ans, m = 0, 0, 0
d[m] = 10**10
for i in range(q) :
    x, y = map(int, input().split())
    if cnt < k :
        if x in d :
            cnt -= 1
            ans -= d[x]
        m = x if d[m] >= y else m
        ans += y
        cnt += 1
        d[x] = y
        topK[x] = True
        print(ans)
        continue
    elif cnt == k :
        if x in d :
            ans -= d[x]
            ans += y
            m = x if d[m] >= y else m
            d[x] = y
            print(ans)
            continue
        else :
            d[x] = y
            cnt += 1
            if m < y :
                topK[x] = True
                topK[m] = False
                ans -= d[m]
                ans += y
                m = x
            print(ans)
            continue
    if x in d :
        if topK[x] :
            if d[m] <= y :
                ans -= d[x]
                ans += y
                topK[m] = False
            else :
                tmp = 0
                for i in range(d) :
                    if topK :
                        continue
                    tmp = max(tmp, d[i])
                ans -= d[x]
                

            d[x] = y
        
            
    elif 
        if 