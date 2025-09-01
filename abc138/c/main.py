#!/usr/bin/env python3
n = int(input())
v_n = list(map(int,input().split()))
v_n.sort()
v_n = [v_n[i]*pow(2,max(0,i-1)) for i in range(n)]
print(sum(v_n)/pow(2,n-1))