#!/usr/bin/env python3
n,l,r = map(int,input().split())
s = input()
print('YNeos'['o'*(r-l+1)!=s[l-1:r]::2])