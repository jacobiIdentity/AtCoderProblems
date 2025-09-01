#!/usr/bin/env python3
n,t = map(int,input().split())        
abi = []
for i in range(n) :
    a,b=map(int,input().split())
    abi.append((-a,b,i))
abiSorted = sorted(abi)
# print(abiSorted)
for i in range(n) :
    print(-t*(abiSorted[0][0]-abi[i][0])+abi[i][1]-abiSorted[0][1])