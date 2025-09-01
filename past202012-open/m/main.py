#!/usr/bin/env python3
import itertools
n,l = map(int,input().split())
a_n = list(map(int,input().split()))
acs = list(itertools.accumulate([0]+a_n))
left,right = 0,l+1
while right-left>1 :
    mid = (left+right)//2
    canCat = [0]*(n+1)
    canCatImos = [0]*(n+1)
    canCatImos[0]=1
    canCatImos[1]=-1
    canCatMin,r = 0,0
    for i in range(n+1) :
        if i>0 :
            canCat[i] = canCat[i-1]+canCatImos[i]
        else :
            canCat[i] = canCatImos[i]
        # i番目ではカットできないので次のiへ
        if canCat[i]==0 :
            continue
        # 今のiについて、カット可能な最初の位置lの場所を探す
        # 各iについて、lは単調増加
        while canCatMin<=n and acs[canCatMin]-acs[i]< mid :
            canCatMin+=1
        
        # l>n の時、カットできない
        if canCatMin>n :
            continue
        
        # 今のiについて、カット不可になる最初の位置(カット可能な一番右の位置+1)を探す
        while r+1<=n and acs[r+1]-acs[i]<=l :
            r+=1
        # imos配列で l~rの範囲に値を更新
        canCatImos[canCatMin] += 1
        if r+1<=n : canCatImos[r+1] -= 1
    canCat[n] = canCat[n-1]+canCatImos[n]
    if canCat[n] > 0 :
        left = mid
    else :
        right = mid
print(left)