#!/usr/bin/env python3
r,c = map(int,input().split())
print([list(map(int,input().split())) for _ in range(2)][r-1][c-1])