#!/usr/bin/env python3
_ = int(input())
ans = sorted(set(map(int,input().split())))
print(len(ans))
print(*ans)