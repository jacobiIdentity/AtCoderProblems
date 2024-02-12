#!/usr/bin/env python3
n, m = map(int, input().split())
cards = sorted(list(map(int, input().split())))
cb = []
for _ in range(m) :
    b, c = map(int, input().split())
    cb.append([c,b])
cb = sorted(cb, key=lambda x: x[0], reverse=True)
ans, i, j, cnt = 0, 0, 0, 0
while i < n :
    if cards[i] < cb[j][0] :
        ans += cb[j][0]
        cnt += 1
    else :
        ans += cards[i]
    i += 1
    if cnt == cb[j][1] :
        cnt = 0
        j += 1
    if j == m :
        break
while i < n :
    ans += cards[i]
    i += 1
print(ans)