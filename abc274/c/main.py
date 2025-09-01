#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
a_n = list(map(int,input().split()))
cnt = defaultdict(int)
cnt[1] = 0
for i in range(1,n+1) :
    cnt[2*i] = cnt[a_n[i-1]]+1
    cnt[2*i+1] = cnt[a_n[i-1]]+1
for i in range(1,2*n+2) :
    print(cnt[i])