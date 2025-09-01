#!/usr/bin/env python3
k = int(input())    
d = dict()
t = 2
while t*t<=k :
    if k%t== 0 :
        cnt = 0
        while k%t==0 :
            cnt+= 1
            k//=t
        d[t]=cnt
    t += 1
if k!=1:
    d[k] = 1
ans = 1
# print(d)
for t in d :
    # ans = max(ans,t*d[t])
    p,tmp = 0,0
    while tmp < d[t] :
        p+=1
        tmp+=1
        if p%t == 0 :
            q = p
            while q%t==0:
                tmp += 1
                q //= t
    # print(t,d[t],tmp,p)
    ans = max(ans,t*p)
print(ans)