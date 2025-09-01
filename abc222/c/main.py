#!/usr/bin/env python3
def gcp(a,b) :
    if a==b :
        return 0
    if (a=="G" and b=="C") or (a=="C" and b=="P") or (a=="P" and b=="G") :
        return 1
    else :
        return -1
n,m = map(int,input().split())
a_ij = [input() for _ in range(2*n)]
ranking = [i for i in range(2*n)]
dNow = {i:0 for i in range(2*n)}
for i in range(m) :
    for k in range(n) :
        result = gcp(a_ij[ranking[2*k]][i],a_ij[ranking[2*k+1]][i])
        if result==1:
            dNow[ranking[2*k]] += 1
        if result==-1:
            dNow[ranking[2*k+1]] += 1
    ranking = sorted(list(range(2*n)),key=lambda x : (-dNow[x],x))
    # print(dNow)
    # print(ranking)
for r in ranking :
    print(r+1)