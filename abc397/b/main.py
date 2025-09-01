#!/usr/bin/env python3
s = list(input())
t = []
for i in range(len(s)) :
    if i == 0 :
        if s[i]=='o' :
            t.append('i')
        # print(1,s[i],t)
    elif t[-1] == s[i] == 'o':
        t.append('i')
        # print(2,s[i],t)
    elif t[-1] == s[i] == 'i':
        t.append('o')
        # print(3,s[i],t)
    t.append(s[i])
if t[-1]== 'i' : t.append('o')
print(len(t)-len(s))