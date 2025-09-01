#!/usr/bin/env python3
n,q = map(int,input().split())
s = input()
sList = [s[i] for i in range(n)]
ABCPoss = set()
for i in range(n-2) :
    if s[i]== 'A' and s[i+1]== 'B' and s[i+2] == 'C' :
        ABCPoss.add(i)

for _ in range(q) :
    xStr,c = input().split()
    x = int(xStr)-1
    # 部分文字列じゃなくなる場合
    if x in ABCPoss and c != 'A' :
        ABCPoss.discard(x)
        sList[x] = c
    elif x-1 in ABCPoss and c != 'B':
        ABCPoss.discard(x-1)
        sList[x] = c
    elif x-2 in ABCPoss and c != 'C':
        ABCPoss.discard(x-2)
        sList[x] = c
    else :
        sList[x] = c

    # 新しく部分文字列になる
    if c == 'A' and x < n-2 :
        if sList[x+1] == 'B' and sList[x+2] == 'C' :
            ABCPoss.add(x)
    elif c == 'B' and 0 < x < n-1 :
        if sList[x-1] == 'A' and sList[x+1] == 'C' :
            ABCPoss.add(x-1)
    elif c == 'C' and 1 < x :
        if sList[x-2] == 'A' and sList[x-1] == 'B' :
            ABCPoss.add(x-2)
    print(len(ABCPoss))    
