#!/usr/bin/env python3
n,s = map(int,input().split())
d = dict()
for _ in range(n) :
    ab = list(map(int,input().split()))
    if len(d)==0:
        d[ab[0]] = ['H']
        d[ab[1]] = ['T']
    else :
        dTmp = dict()
        for num in d :
            for i in range(2) :
                if num+ab[i] <= s:
                    dTmp[num+ab[i]] = d[num]+['HT'[i]]
        d = dTmp
print('YNeos'[s not in d ::2])
if s in d :
    print(''.join(d[s]))
