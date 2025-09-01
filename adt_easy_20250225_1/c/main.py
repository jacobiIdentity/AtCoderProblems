#!/usr/bin/env python3
n = int(input())
for i in range(n,1000) :
    a,b,c = int(str(i)[0]),int(str(i)[1]),int(str(i)[2])
    if a*b == c :
        print(i)
        exit()