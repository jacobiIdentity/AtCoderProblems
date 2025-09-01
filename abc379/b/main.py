#!/usr/bin/env python3
n,k = map(int,input().split())
s = input()
ans = 0
now = 0
while now < n-k+1 :
    # print(now,'O'*k,s[now:now+k],s[now:now+k] == 'O'*k)
    if s[now:now+k] == 'O'*k :
        ans += 1
        now += k
    else :
        now += 1
print(ans)
        