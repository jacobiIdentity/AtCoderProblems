#!/usr/bin/env python3
n, tPrime = input().split()
n = int(n)
tLen = len(tPrime)
ans = []
for i in range(n) :
    t = input()
    if len(t) == tLen :
        diffCnt = 0
        for j in range(tLen) :
            if tPrime[j] != t[j] :
                diffCnt += 1
        if diffCnt < 2 :
            ans.append(i+1)
    elif len(t) == tLen+1 :
        diffCnt = 0
        for j in range(len(t)) :
            if diffCnt > 1 :
                break
            if diffCnt == 0 and j == len(t)-1 :
                diffCnt += 1
                break
            if tPrime[j-diffCnt] != t[j] :
                diffCnt += 1
        if diffCnt < 2 :
            ans.append(i+1)
    elif len(t) == tLen-1 :
        diffCnt = 0
        for j in range(tLen):
            if diffCnt > 1 :
                break
            if diffCnt == 0 and j == tLen-1 :
                diffCnt += 1
                break
            if tPrime[j] != t[j-diffCnt] :
                diffCnt += 1
        if diffCnt < 2 :
            ans.append(i+1)
print(len(ans))
print(*ans)

    