#!/usr/bin/env python3
a,b,c = map(int,input().split())
circ = []
tmp = a%10
while tmp not in circ :
    circ.append(tmp)
    tmp *= a
    tmp %= 10
# print(circ)
print(circ[(pow(b,c,len(circ))-1)%len(circ)])
