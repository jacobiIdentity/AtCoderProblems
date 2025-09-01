#!/usr/bin/env python3
n = int(input())
h_n = list(map(int,input().split()))
arr = [(h_n[i],i+1) for i in range(n) ]
arr.sort()
ans = [arr[i][1] for i in range(n)]
print(*ans)
