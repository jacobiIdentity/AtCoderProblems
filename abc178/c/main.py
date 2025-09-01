#!/usr/bin/env python3
n = int(input())
print((pow(10,n,10**9+7)+pow(8,n,10**9+7)-pow(9,n,10**9+7)*2)%(10**9+7))