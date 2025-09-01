#!/usr/bin/env python3
n = int(input())
s_n = [input() for _ in range(n)]
ans = 0
b_acnt, aCnt,bCnt = 0,0,0
for i in range(n) :
    ans += s_n[i].count('AB')
    if s_n[i][0]=='B' and s_n[i][-1]=='A' :
        b_acnt += 1
    elif s_n[i][0]=='B' :
        bCnt += 1
    elif s_n[i][-1]=='A' :
        aCnt += 1
# print(ans,b_acnt,aCnt,bCnt)
if b_acnt > 0 :
    ans += b_acnt-1
    if aCnt > 0 :
        ans += 1
        aCnt -= 1
    if bCnt > 0 :
        ans += 1
        bCnt -= 1
ans += min(aCnt,bCnt)    
print(ans)