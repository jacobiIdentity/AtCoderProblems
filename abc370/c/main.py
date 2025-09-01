#!/usr/bin/env python3
s = input()
t = input()
x = []
now = 0
skipNum = []
while now < len(s) :
    if s[now] != t[now] :
        if now == len(s)-1 :
            s = s[:now]+t[now]
            x.append(s)
        elif ord(s[now]) > ord(t[now]) :
            s = s[:now]+t[now]+s[now+1:]
            x.append(s)
        else :
            skipNum.append(now)
    now += 1
while skipNum :
    now = skipNum.pop()
    s = s[:now]+t[now]+s[now+1:]
    x.append(s)
print(len(x))
print(*x, sep='\n')

