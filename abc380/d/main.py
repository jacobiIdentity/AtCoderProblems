#!/usr/bin/env python3
def isS(num) :
    if num == 0 :
        return True
    elif num == 1 :
        return False
    else :
        pow2 = 1
        # tmp = num
        # while tmp> 1 :
        #     tmp //= 2
        #     pow2 *= 2

        # pow2 = 2**(len(format(num,'b'))-1)
        for _ in range(len(format(num,'b'))-1) :
            pow2 *= 2
        return not(isS(num%(pow2)))
s = list(input()) 
q = int(input())
k_q = list(map(int,input().split()))
t = [ss.lower() if ss.isupper() else ss.upper() for ss in s]
ans = []

print(*[s[(k-1)%len(s)] if isS((k-1)//len(s)) else t[(k-1)%len(s)] for k in k_q])
# for k in k_q :
#     ans.append(s[(k-1)%len(s)] if isS((k-1)//len(s)) else t[(k-1)%len(s)])

# print(*ans)

