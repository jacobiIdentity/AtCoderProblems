#!/usr/bin/env python3
n = int(input())
cards = []
for i in range(n) :
    a, c = map(int,input().split())
    cards.append((c,a,i+1))
cards.sort(key=lambda x:x[0])
ans = set()
tmpC,tmpA = 0,0
for i in range(n) :
    if tmpA < cards[i][0] and tmpC < cards[i][1] :
        ans.add(cards[i][2])
        tmpA = cards[i][0]
        tmpC = cards[i][1]
print(len(ans))
print(*sorted(list(ans)))
    