#!/usr/bin/env python3
l,r = map(int,input().split())
s = list(input())
print(''.join(s[:l-1]+[s[i] for i in reversed(range(l-1,r))]+s[r:]))