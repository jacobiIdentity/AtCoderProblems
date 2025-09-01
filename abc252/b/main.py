#!/usr/bin/env python3
n,k = map(int,input().split())
a_n = list(map(int,input().split()))
b_k = set(map(int,input().split()))
a_n_withI = [(a_n[i],i+1) for i in range(n)]
# print(a_n_withI)
a_n_withI.sort(key= lambda x:(-x[0],x[1]))
maxA = a_n_withI[0][0]
candidates = set()
isNo = True
for i in range(n) :
    if a_n_withI[i][0]==maxA  and a_n_withI[i][1] in b_k:
        isNo = False
        candidates.add(a_n_withI[i][1])
print('YNeos'[isNo::2])
# print('YNeos'[len(b_k&candidates)==0::2])

