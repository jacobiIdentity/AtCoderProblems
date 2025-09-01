#!/usr/bin/env python3
_,k=map(int,input().split())
print(sum(sorted(list(map(int,input().split())))[:k]))