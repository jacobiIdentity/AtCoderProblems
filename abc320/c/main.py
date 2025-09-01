#!/usr/bin/env python3
import itertools
m = int(input())
s_i = [input() for _ in range(3)]
ans = float('inf')
for i in range(10) :
    for perm in itertools.permutations([0,1,2]) :
        cnt = 0
        now = 0
        for j in perm :
            tmp = 0
            isNG = True
            while tmp < m :
                if s_i[j][cnt]==str(i) :
                    isNG = False
                tmp += 1
                cnt += 1
                cnt %= m
                if not(isNG) :
                    now += tmp
                    break
            if isNG :
                break
        if not(isNG) :
            ans = min(ans,now)
if ans == float('inf') :
    ans = 0
ans -=1
print(ans)
