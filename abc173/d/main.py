#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
a_n.sort()
a_n.reverse()
ans = a_n[0]+2*sum(a_n[1:n//2])
ans += a_n[n//2] if n%2 != 0 else 0
print(ans)