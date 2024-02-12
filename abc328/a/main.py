#!/usr/bin/env python3
n, x = map(int,input().split())
print(sum(filter(lambda s:s<=x,map(int, input().split())) ))