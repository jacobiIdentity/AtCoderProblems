#!/usr/bin/env python3
n,m = map(int,input().split())
candidates = []
for dig in range(1,10) :
    div = 1
    i = 1
    while i*i <= min(m,dig) :
        if m%i==0 and dig%i==0 :
            div = max(div,i)
            if m%(dig//i)==0 :
                div = max(div,dig//i)
            if dig%(m//i)==0 :
                div = max(div,m//i)
        i += 1
    base = m//div
    # print(m,dig,div,base)        
    now = 0
    for i in range(n) :
        now *= 10
        now += 1
        now %= base
        if now == 0 :
            candidates.append((i+1,dig))
            # ans = max(ans,int(str(dig)*(i+1)))
# print(candidates)
if len(candidates) == 0 :
    ans = '-1'
else :
    length,digit = max(candidates)
    ans = str(digit)*length

print(ans)