#!/usr/bin/env python3
n,q = map(int,input().split())
a_n = [i+1 for i in range(n)]
stt = 0
for _ in range(q) :
    query = list(map(int,input().split()))
    if query[0]==1 :
        p,x = query[1],query[2]
        a_n[(p-1+stt)%n] = x
    elif query[0]==2 :
        p = query[1]
        print(a_n[(p-1+stt)%n])
    else :
        stt += query[1]