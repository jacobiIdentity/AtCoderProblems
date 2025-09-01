#!/usr/bin/env python3
a = int(input())
n = int(input())
digs = len(str(n))
ps = set(range(min(10,n+1)))
ans = 0
for i in range(1,10**(digs//2)) :
    p = int(str(i)+str(i)[::-1])
    if p > n :
        break
    ps.add(p)
    for j in range(10) :
        p = int(str(i)+str(j)+str(i)[::-1])
        if p>n :
            break
        ps.add(p)
# print(ps)
# print(len(ps))
for p in ps :
    q = p
    tmp = []
    while q :
        tmp.append(q%a)
        q //= a
    isP = True
    for i in range(len(tmp)//2) :
        if tmp[i] != tmp[len(tmp)-i-1] :
            isP = False
            break
    if isP :
        ans += p
print(ans)