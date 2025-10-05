#!/usr/bin/env python3
t = int(input())
for _ in range(t) :
    n = int(input())
    s = list(input())
    cnt0 = s.count('0')
    cnt1 = n-cnt0
    maxBlock0Cnt = 0
    maxBlock1Cnt = 0
    i = 0
    while i < n :
        j = i
        while j < n and s[j]==s[i] :
            j += 1
        l = j-i
        if s[i] == '1' :
            maxBlock1Cnt = max(l,maxBlock1Cnt)
        else :
            maxBlock0Cnt = max(l,maxBlock0Cnt)
        i=j
    print(min(2*(cnt1-maxBlock1Cnt)+cnt0,2*(cnt0-maxBlock0Cnt)+cnt1))