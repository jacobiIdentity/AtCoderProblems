#!/usr/bin/env python3
a,b,c = map(int,input().split())
print(max(0,b+c-a))
# print(b+c-min(a,b+c))