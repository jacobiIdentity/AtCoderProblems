#!/usr/bin/env python3
from collections import deque
n = int(input())
s = input()
q = deque()
i, fCnt = 0, 0
while i < n :
    # print('q: '+ str(q))
    q.append(s[i])
    if s[i] == '(' :
        fCnt += 1
    elif s[i] == ')' :
        if fCnt != 0 :
            while True :
                if q.pop() == '(' :
                    break
            fCnt -= 1
    i += 1
print(*q, sep="")
