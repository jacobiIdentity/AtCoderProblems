#!/usr/bin/env python3
def isS(num) :
    # print(num,div)
    if num == 0 :
        return True
    elif num == 1 :
        return False
    else :
        pow2 = 2
        tmp = num
        while tmp> 1 :
            tmp //= 2
            pow2 *= 2
            # print(tmp)
        # print(num,pow2)
        return not(isS(num%(pow2//2)))   
s = list(input()) 
q = int(input())
k_q = list(map(int,input().split()))
t = [ss.lower() if ss.isupper() else ss.upper() for ss in s]
# print(s)
# print(t)
ans = []

for i in range(20) :
    print('S' if isS(i) else 'T',end=" ")
# for k in k_q :
#     kDig = 
#     if is
    
