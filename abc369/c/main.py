#!/usr/bin/env python3
import itertools
n = int(input())
a_n = list(map(int,input().split()))
diff = [a_n[i+1]-a_n[i] for i in range(n-1)]
before, cnt, ans = -1, 0, 2*n-1
for i in range(n-1) :
    if before == -1 :
        cnt = 1
    elif before != diff[i] :
        if cnt >= 2 :
            ans += (cnt)*(cnt-1)//2
        cnt = 1
    else :
        cnt += 1
        if i == n-2 :
            ans += (cnt)*(cnt-1)//2
    before = diff[i]
            

print(ans)