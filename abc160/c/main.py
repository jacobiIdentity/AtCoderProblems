#!/usr/bin/env python3
k,n = map(int,input().split())
a_n = list(map(int,input().split()))
b_n = [(a_n[(i+1)%n]-a_n[i])%k for i in range(n)]
print(sum(b_n)-max(b_n))
