#!/usr/bin/env python3
n = int(input())
d = [input() for i in range(n)]
# d = {str(i+1):input() for i in range(n)}
x,y = input().split()
print("YNeos"[not(d[int(x)-1]==y)::2])