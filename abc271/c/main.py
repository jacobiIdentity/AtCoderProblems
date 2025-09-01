#!/usr/bin/env python3
from collections import deque
n = int(input())
a_n = list(map(int, input().split()))
mangas = set()
daburi = 0
for i in range(n) :
    a = a_n[i]
    if a_n[i] in mangas :
        daburi += 1
        a = 10**9+daburi
    mangas.add(a)
# print(daburi,mangas)
q = deque()
for m in sorted(list(mangas)) :
    q.append(m)
ans = 0
while q :
    tmp = q.popleft()
    if tmp == ans+1 :
        ans += 1
        continue
    q.appendleft(tmp)
    if len(q)>1 :
        q.pop()
        q.pop()
        ans +=1
    else :
        break
print(ans)