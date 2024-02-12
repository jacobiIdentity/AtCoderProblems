#!/usr/bin/env python3
from collections import deque
n = int(input())
a_n = []
for _ in range(n) :
    c = input()
    a_n.append(set(map(int, input().split())))
x = int(input())
q = deque()
size = 10000
for i in range(n) :
    if x in a_n[i] :
        size = min(len(a_n[i]),size)
        q.append((i+1, len(a_n[i])))
ans = []
while q :
    t = q.popleft()
    if t[1] <= size :
        ans.append(t[0])
ans.sort()
print(len(ans))
print(*ans)