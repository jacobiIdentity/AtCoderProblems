#!/usr/bin/env python3
from collections import defaultdict
n = int(input())
s = input()
q = int(input())
alphabets = 'abcdefghijklmnopqrstuvwxyz'
changes = {t:t for t in alphabets}
for _ in range(q) :
    c,d = input().split()
    for t in alphabets :
         if changes[t] == c :
               changes[t] = d
for i in range(n) :
    print(changes[s[i]], end="")
    if i == n-1 :
        print()