#!/usr/bin/env python3
n,k = map(int,input().split())
a_n = list(map(int,input().split()))
b_n = list(map(int,input().split()))
aIsOK,bIsOK = True,True
for i in range(1,n) :
    tmpAFlg,tmpBFlg = True,True
    if not((aIsOK and abs(a_n[i]-a_n[i-1])<=k) or (bIsOK and abs(a_n[i]-b_n[i-1])<=k)) :
        tmpAFlg = False
    if not((aIsOK and abs(b_n[i]-a_n[i-1])<=k) or (bIsOK and abs(b_n[i]-b_n[i-1])<=k)) :
        tmpBFlg = False
    aIsOK = tmpAFlg
    bIsOK = tmpBFlg
    if not(aIsOK or bIsOK) :
        print('No')
        exit()
print('Yes')

