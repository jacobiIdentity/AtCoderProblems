#!/usr/bin/env python3
n,t,p = map(int,input().split())
l_n = list(map(int,input().split()))
l_n.sort()
l_n.reverse()
print(max(0,t-l_n[p-1]))
