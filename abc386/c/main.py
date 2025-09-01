#!/usr/bin/env python3
k = int(input())
s = input()
t = input()
if abs(len(s)-len(t)) > 1 :
    print('No')
    exit()
if len(s) != len(t) :
    if len(s) > len(t) :
        s, t = t, s
    for i in range(len(s)) :
        if s[i] != t[i] :
            if s[:i]+t[i]+s[i:] == t :
                print('Yes')
                exit()
            else :
                print('No')
                exit()
    print('Yes')
    exit()
difCnt = 0
for i in range(len(s)) :
    if s[i] != t[i] :
        difCnt += 1
print('Yes' if difCnt < 2 else 'No')