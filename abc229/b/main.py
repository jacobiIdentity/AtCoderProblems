#!/usr/bin/env python3
a,b = map(int, input().split())
c = a+b
aStr,bStr,cStr = str(a),str(b),str(c)
if max(len(aStr),len(bStr)) < len(cStr) :
    print('Hard')
    exit()
for i in range(len(cStr)) :
    if len(aStr)-i-1>-1 and aStr[len(aStr)-i-1] > cStr[len(cStr)-i-1] :
        print('Hard')
        exit()
    if len(bStr)-i-1>-1 and bStr[len(bStr)-i-1] > cStr[len(cStr)-i-1] :
        print('Hard')
        exit()
print('Easy')