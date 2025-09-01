#!/usr/bin/env python3
s = input()
ans = 0
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
now = s.find(alphabets[0])
for i in range(25) :
    ans += abs(s.find(alphabets[i+1]) -now)
    now = s.find(alphabets[i+1])
print(ans)
