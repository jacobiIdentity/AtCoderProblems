#!/usr/bin/env python3
ans = 0 
for i in range(1,13) :
    ans += 1 if len(input()) == i else 0
print(ans)