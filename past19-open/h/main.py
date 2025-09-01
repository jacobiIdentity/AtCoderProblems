#!/usr/bin/env python3
import itertools
n,s = map(int,input().split())
a_n = input().split()
isNo = True
for a_n2 in itertools.permutations(a_n) :
    for i in range(1<<n) :
        bI = format(i, '0'+str(n)+'b')
        evalStr = a_n2[0]
        for j in range(1,n) :
            evalStr += ('+' if bI[j]=='1' else '*') + a_n2[j]
        if eval(evalStr)== s :
            print('Yes')
            print(evalStr.replace("*","x"))
            exit()
print('No')
