#!/usr/bin/env python3
n, m = map(int, input().split())
a_n = sorted(list(map(int, input().split())))
now, base, tmp, ans = 0, 0, 0, 0
while now < n :
    if a_n[now] < a_n[base] + m :
        tmp += 1
        now += 1
    else :
        ans = max(ans, tmp)
        while base <= now :
            if a_n[now] < a_n[base] + m :
                break
            else :
                base += 1
                tmp -= 1
print(max(ans, tmp))