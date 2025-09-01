#!/usr/bin/env python3
import itertools
n,c = map(int,input().split())
a_n = list(map(int,input().split()))
acs = [0]+ list(itertools.accumulate(a_n))
# print(a_n)
# print(acs)
if c>1 :
    acs_i = [(-acs[i],-i) for i in range(n+1)]
    # print(acs_i)
    acs_i.sort()
    left,right = 0,-acs_i[0][1]
    ans = max(acs[right]-acs[left],0)
    rPos = 0
    while right<n+1 :
        isEnd = False
        if left ==right :
            # print(left,ans)
            i = rPos
            while i <n+1 :
                if -acs_i[rPos][1] < -acs_i[i][1] :
                    rPos = i
                    right = -acs_i[rPos][1]
                    break
                i+=1
            if i==n+1 :
                isEnd = True
        if isEnd :
            break
        ans = max(acs[right]-acs[left],ans)
        left += 1
else :
    acs_i = [(acs[i],-i) for i in range(n+1)]
    # print(acs_i)
    acs_i.sort()
    left,right = 0,-acs_i[0][1]
    ans = min(acs[right]-acs[left],0)
    rPos = 0
    while right<n+1 :
        isEnd = False
        if left ==right :
            # print(left,ans)
            i = rPos
            while i <n+1 :
                if -acs_i[rPos][1] < -acs_i[i][1] :
                    rPos = i
                    right = -acs_i[rPos][1]
                    break
                i+=1
            if i==n+1 :
                isEnd = True
        if isEnd :
            break
        ans = min(acs[right]-acs[left],ans)
        left += 1


ans *= c-1
ans += sum(a_n)
print(ans)

