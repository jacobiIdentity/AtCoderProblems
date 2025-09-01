#!/usr/bin/env python3
n = int(input())
print('Yes' if len(set(map(int,input().split())))==1 else 'No')