#!/usr/bin/env python3
n,k = list(map(int,input().split()))
a_n = list(map(int,input().split()))
left,right = 0,0
ans,tmp = 0,0
while right < n :
    tmp += a_n[right]
    if tmp >= k :
        while right-left>=0 :
            # print(left,right,tmp)
            if tmp<k :
                break
            ans += n-right
            tmp -= a_n[left]
            left += 1
    right += 1
print(ans)