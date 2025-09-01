#!/usr/bin/env python3
n,t,p = map(int,input().split())
print(max(t-sorted(list(map(int,input().split())),reverse=True)[p-1],0))

