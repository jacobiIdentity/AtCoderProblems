#!/usr/bin/env python3
n,q = map(int,input().split())
a_n = list(map(int,input().split()))
b_n = list(map(int,input().split()))
d = dict()
ans = 0
for i in range(n) :
    d[i] = min(a_n[i],b_n[i])
    ans += d[i]
# print(d)
# print(ans)
for _ in range(q) :
    c,x,v = input().split()
    x = int(x)-1
    v = int(v)
    if c == "A" :
        a_n[x] = v
    else :
        b_n[x] = v
    # print(a_n)
    # print(b_n)
    ans += min(a_n[x],b_n[x]) - d[x]
    d[x] = min(a_n[x],b_n[x])
    print(ans)    