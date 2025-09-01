#!/usr/bin/env python3
n,k = map(int,input().split())
# cards = {i:set(range(1,k+1)) for i in range(1,n+1)}
cards2 = {i:k for i in range(1,n+1)}
fixed = set()
for i in range(1,k+1) :
    c,ki = input().split()
    ki = int(ki)
    fixed.add(ki)
    # cards[ki] = {i}
    cards2[ki] = 1
    if c == 'L' :
        for j in range(1,ki) :
            if j in fixed :
                continue
            # cards[j].discard(i)
            cards2[j] -= 1
    else :
        for j in range(ki+1,n+1) :
            if j in fixed :
                continue
            # cards[j].discard(i)
            cards2[j] -= 1
# ans = 1
ans2 = 1
for i in range(1,n+1) :
    # ans *= len(cards[i])
    # ans %= 998244353
    ans2 *= cards2[i]
    ans2 %= 998244353
# print(ans)
print(ans2)
# print(cards)
# print(cards2)