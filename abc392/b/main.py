#!/usr/bin/env python3
n,m = map(int,input().split())
a_m = set( map(int,input().split()))
ans = list(set(range(1,n+1))-a_m)
ans.sort()
print(len(ans))
print(*ans)
