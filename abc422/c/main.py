#!/usr/bin/env python3
t = int(input())
for _ in range(t) :
    n_a,n_b,n_c = map(int,input().split())
    tmp = min(n_a,n_c)
    n_a -= tmp
    n_c -= tmp
    ans = min(tmp,n_a+n_b+n_c)
    tmp -= ans
    if tmp >= 0 :
        ans += (tmp//3)*2
        tmp %= 3
        if tmp == 2:
            ans += 1
    print(ans)