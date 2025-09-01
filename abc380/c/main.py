#!/usr/bin/env python3
n,k = map(int,input().split())
s = input()
massCnt = 0
isInMass = False
kMinus1Start,kMinus1End, kStart, kEnd = 0,0,0,0
for i in range(n) :
    # 塊の開始位置の時
    if not(isInMass) and s[i] == '1' :
        isInMass = True
        massCnt += 1
        # k-1こめ
        if massCnt == k-1 :
            kMinus1Start =i
        # kこめ
        if massCnt == k :
            kStart = i
    # 塊の終わり 
    if isInMass and s[i] == '0' :
        # k-1こめ
        if massCnt == k-1 :
            kMinus1End = i-1
        # kこめ
        if massCnt == k :
            kEnd = i-1
        isInMass = False
# 塊の終わり 
if isInMass and massCnt == k-1 :
    kMinus1End = n-1
    # kこめ
if isInMass and massCnt == k :
    kEnd = n-1
# print(kMinus1Start,kMinus1End,kStart,kEnd)
# print('k-1個めの塊まで:',s[:kMinus1End+1])
# print('k  個目の塊全量',s[kStart:kEnd+1])
# print('k-1とkの間'+s[kMinus1End+1:kStart])
# print(''+s[kEnd+1:])
print(s[:kMinus1End+1]+s[kStart:kEnd+1]+s[kMinus1End+1:kStart]+s[kEnd+1:])
