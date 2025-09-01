#!/usr/bin/env python3
r,g,b = map(int,input().split())
c = input()
ans = [r,g,b]
ans.remove(r if c == 'Red' else (b if c == 'Blue' else g))
print(min( ans))
