#!/usr/bin/env python3
n,m = map(int,input().split())
a_n = list(map(int,input().split()))
dp = [[0]*m for _ in range(n)]
