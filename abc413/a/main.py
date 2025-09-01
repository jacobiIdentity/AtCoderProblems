#!/usr/bin/env python3
n,m = map(int,input().split())
print('YNeos'[sum(map(int,input().split()))>m::2])