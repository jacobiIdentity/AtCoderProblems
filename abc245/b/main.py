#!/usr/bin/env python3
n = int(input())
a_n = set(map(int,input().split()))
for i in range(2001) :
    if i not in a_n :
        print(i)
        exit()