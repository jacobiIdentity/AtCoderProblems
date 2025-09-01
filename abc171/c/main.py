#!/usr/bin/env python3
# for n in range(1,1001) :
#     ans = ''
#     while True :
#         ans = chr(ord('a')+n%27-1) + ans
#         if n//27 > 0 :
#             n //= 27
#         else :
#             break
    # print(ans)

n = int(input())
ans = ''
while True :
    ans = chr(ord('a')+(n-1)%26+1-1) +ans
    if (n-1)//26 > 0 :
        n = (n-1)//26
    else :
        break
print(ans)

