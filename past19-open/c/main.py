#!/usr/bin/env python3
def isG(dig) :
    for i in range(len(dig)-1) :
        if abs(dig[i]-dig[i+1]) > 1 :
            return False
    return True
        
n = int(input())
digits = list(map(int,list(str(n))))
# digits = [digits[0]]+digits+[digits[-1]]
# print(digits)
gap = 0
isNo = True
for i in range(len(digits)) :
    for j in range(10) :
        if i == j == 0 : continue
        if isG(digits[:i]+[j]+digits[i+1:]) :
            # print(i,j,digits[:i]+[j]+digits[i+1:])
            isNo = False
            break
    if not(isNo) :
        break
print('YNeos'[isNo::2])