#!/usr/bin/env python3
n = int(input())
ans = set()
div = 1
while div*div < n+1 :
    if n%div == 0 :
        ans.add(div)
        ans.add(n//div)
    div += 1
print(*sorted(list(ans)),sep='\n')