#!/usr/bin/env python3
n,m = map(int ,input().split())
schedules =  input().split('0')
ans, tmp = 0, m
for s in schedules :
    muji,logo = 0,0
    for t in s :
        if t == '2' :
            logo += 1
        else :
            muji += 1
    ans = max(ans, logo+max(0,muji-m))
print(ans)