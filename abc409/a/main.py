#!/usr/bin/env python3
n = int(input())
t = input()
a = input()
isNo = True
for i in range(n) :
    if t[i]==a[i]=="o" :
        isNo =False
print("YNeos"[isNo::2])