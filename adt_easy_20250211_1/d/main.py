#!/usr/bin/env python3
n,x,y,z = map(int,input().split())
a_n = list(map(int,input().split()))
b_n = list(map(int,input().split()))
ans = sorted(list(range(1,n+1)),key=lambda i:(-a_n[i-1],i))[:x]
ans += sorted(list(set(range(1,n+1))-set(ans)),key=lambda i:(-b_n[i-1],i))[:y]
ans += sorted(list(set(range(1,n+1))-set(ans)),key=lambda i:(-a_n[i-1]-b_n[i-1],i))[:z]
print(*sorted(ans),sep="\n")