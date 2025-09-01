#!/usr/bin/env python3
s = input()
k = int(input())
ans = 0
left,right,cost = 0,0,0
while left < len(s) :
# for left in range(len(s)) :
    # right = left
    # cost = 0
    while right < len(s) :
        if s[right] == '.' :
            cost += 1
            if cost > k :
                ans = max(right-left,ans)
                break
        right += 1
    # print(left,right,cost)
    if cost < k+1 :
        ans = max(right-left,ans)
    while left < len(s) :
        if s[left] == '.' :
            cost -= 1
            left += 1
            break
        else :
            left += 1
    right += 1
print(ans)
    
