#!/usr/bin/env python3
n = int(input())
SweetyBefore = False
isYes = True
for i in range(n) :
    if input() == 'sweet' :
        # print(i,isYes,SweetyBefore)
        if SweetyBefore and i < n-1:
            isYes = False
            break
        else :
            SweetyBefore = True
    else :
        SweetyBefore = False
print('Yes' if isYes else 'No')