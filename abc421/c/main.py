#!/usr/bin/env python3
n = int(input())
s = input()
aPos = []
for i in range(2*n):
    if s[i]=="A" :
        aPos.append(i)
tmp1,tmp2 = 0,0
for i in range(n) :
    tmp1 += abs(aPos[i]-2*i)
    tmp2 += abs(aPos[i]-2*i-1)
print(min(tmp1,tmp2))