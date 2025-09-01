#!/usr/bin/env python3
n,l = map(int,input().split())
print(len(list(filter(lambda x:x>=l,map(int,input().split())))))