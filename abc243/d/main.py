#!/usr/bin/env python3
n,x = map(int,input().split())
s = input()
ansStr = list(bin(x)[2:])
for ss in s :
    if ss == 'U' :
        ansStr.pop()
    elif ss == 'L' :
        ansStr.append('0')
    else :
        ansStr.append('1')
print(int('0b'+''.join(ansStr),base=2))
