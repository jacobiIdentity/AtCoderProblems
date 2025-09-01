#!/usr/bin/env python3
n,m = map(int,input().split())
s = input()
t = input()
p = (t[:n]==s)*2
s = (t[(m-n):]==s)
print(3-p-s)