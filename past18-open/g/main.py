#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
b_n = list(map(int,input().split()))
exchageCnt = 0
i = 0
isOK = True
while i < n :
    if a_n[i] != b_n[i] :
        if exchageCnt < 2 and i+1<n and b_n[i]==a_n[i+1] and b_n[i+1]==a_n[i] :
            exchageCnt += 1
            i += 2
            continue
        else :
            isOK = False
            break
    i += 1
if exchageCnt in [0,2] and isOK :
    print("Yes")
    exit()
isOK = True
exchageCnt = 0
i = 0
while i < n :
    if a_n[i] != b_n[i]:   
        if exchageCnt==0 and i+2<n : 
            if (b_n[i]==a_n[i+1] and b_n[i+1]==a_n[i+2] and b_n[i+2]==a_n[i]) \
                or (b_n[i]==a_n[i+2] and b_n[i+1]==a_n[i] and b_n[i+2]==a_n[i+1]) :
                exchageCnt += 2
                i += 3
                continue
        else :
            isOK = False
            break
    i += 1
if exchageCnt == 2 and isOK :
    print("Yes")
else :
    print('No')