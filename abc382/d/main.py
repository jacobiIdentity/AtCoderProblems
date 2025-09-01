#!/usr/bin/env python3
n,m= map(int,input().split())
cnt = [0]*(m+1)
mMod10 = (m-1)%10+1
for i in range(m+1) :
    if 1 <= i <= mMod10 :
        cnt[i] = 1
        continue
    if 1 <= (i-1)%10+1 <= mMod10 :
        tmp = 0
        for j in range((i-1)%10+1) :
            tmp += cnt[10*((i-1)//10-1)+j+1]
        cnt[i] = tmp
lenX = 0
for i in range(10*((m-1)//10)+1,m+1):
    lenX += cnt[i]
print(lenX)
ans = [1]
isEnd = False
while len(ans)>0 :
    if len(ans) < n :
        ans.append(ans[-1]+10)
    if len(ans) == n :
        print(*ans)
        while 0<len(ans) :
            if (ans[-1]-1)%10+1 == mMod10 :
                ans.pop()
            else :
                tmp = ans.pop()
                ans.append(tmp+1)
                break
