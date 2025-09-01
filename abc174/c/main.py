#!/usr/bin/env python3
k = int(input())
if k%7 == 0 :
    k //= 7
k *= 9
i,now = 0,1
ans = -1
already = set()
while True :
    now *= 10
    now %= k
    i += 1
    if now == 1 :
        ans = i
        break
    if now in already :
        break
    already.add(now)
print(ans)