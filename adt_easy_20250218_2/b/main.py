#!/usr/bin/env python3
abcd = sorted(list(map(int,input().split())))
isY = False
if (abcd[0] == abcd[1] == abcd[2] and abcd[2] != abcd[3]) \
  or (abcd[0] != abcd[1] and  abcd[1] == abcd[2] == abcd[3]) \
  or (abcd[0] == abcd[1] and abcd[1] !=  abcd[2] and abcd[2] == abcd[3])  :
    isY = True
print('YNeos'[not(isY)::2])