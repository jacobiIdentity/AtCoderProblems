#!/usr/bin/env python3
from collections import deque
import heapq
n = int(input())
times = []
for _ in range(n) :
    t, d = map(int, input().split())
    times.append((t, t+d))
times.sort(key=lambda x:(x[0], x[1]))
# print(times)
# que = deque(times)
# tmp, now, ans = 0, 1, 0
# while que :
#     tmp = que.popleft()
#     if tmp[0] > now :
#         now = tmp[0]+1
#         print("if tmp[0] > now :", tmp)
#         ans += 1
#     elif tmp[0] == now :
#         now += 1
#         ans += 1
#         print("elif tmp[0] == now :", tmp)
#     elif tmp[0] < now and now <= tmp[1] :
#         now += 1
#         ans += 1
#         print("elif tmp[0] < now and tmp[1] <= now :", tmp)
#     else :
#         now += 1
#         print("else :", tmp)
# print(ans)
que = []
heapq.heapify(que)
i, t, ans = 0, 1, 0
while i < n :
    if len(que) == 0 :
        if i == n :
            break
        t = times[i]
    while i < n and times[i][0] == t :
        heapq.heappush(que, times[i][1])
        i += 1
    while len(que) > 0 and que[0] < i :
        heapq.heappop(que)
    if len(que) > 0 :
        heapq.heappop(que)
        ans += 1
print(ans)