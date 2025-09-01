#!/usr/bin/env python3
a,b = map(int, input().split())
ans = set()
ans.add(2*b-a)
ans.add(2*a-b)
if (a+b)%2== 0 :
    ans.add((a+b)//2)
print(len(ans))