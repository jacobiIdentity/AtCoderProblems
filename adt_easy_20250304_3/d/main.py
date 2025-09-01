#!/usr/bin/env python3
k = int(input())
aKStr,bKStr = input().split()
a = 0
for i in range(len(aKStr)) :
    a += int(aKStr[i])*(k**(len(aKStr)-i-1))
# print(aKStr,a)
b = 0
for i in range(len(bKStr)) :
    b += int(bKStr[i])*(k**(len(bKStr)-i-1))
print(a*b)
