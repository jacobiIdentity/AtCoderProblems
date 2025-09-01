#!/usr/bin/env python3
num = {'A','2','3','4','5','6','7','8','9','T','J','Q','K'}
suit = {'H','D','C','S'}
n = int(input())
done = set()
isN = False
for _ in range(n) :
    s = input()
    if not(s[0] in suit and s[1] in num and s not in done) :
        isN = True
        break
    done.add(s)
print('YNeos'[isN::2])