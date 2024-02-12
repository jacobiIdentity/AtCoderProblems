#!/usr/bin/env python3
from collections import deque
n = int(input())
tmp = n
cnt = 0
while tmp > 0 :
    tmp //= 2
    cnt += 1
print(n*cnt-(2**cnt-n%(2**cnt)))
# ans = 0
# q = deque()
# q.append(n)
# while q :
#     t = q.popleft()
#     ans += t
#     if t//2 > 1 :
#         q.append(t//2)
#     if t//2+t%2 > 1 :
#         q.append(t//2+t%2)
# print(ans)