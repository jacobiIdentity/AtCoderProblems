#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
print(sum([max(a-10,0) for a in a_n]))