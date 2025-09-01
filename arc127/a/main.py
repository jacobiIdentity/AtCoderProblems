#!/usr/bin/env python3
n = int(input())
l =len(str(n))
if l == 1 :
    print(1)
    exit()
dp = [[0]*(l+1) for _ in range(l+1)]
dp[1][1] = 1
for i in range(2,l+1) :
    for j in range(1,i+1) :
        if j==i :
            dp[i][j] = dp[i-1][j-1]
        elif j==i-1 :
            dp[i][j] = dp[i-1][j]*9
        else :
            dp[i][j] = dp[i-1][j]*10
# print(dp)
ans = 0
for i in range(l+1) :
    if i<l:
        for j in range(i+1) :
            ans += dp[i][j]*j
# print(ans)
pos = 0
while pos < l :
    # print(pos,str(n)[pos])
    if str(n)[pos]=='0' :
        ans += (int(str(n)[pos:])+1)*pos
        break
    elif str(n)[pos]>='2' :
        ans += (10**(l-pos-1) + int(str(n)[pos:])-2*10**(l-pos-1)+1)*pos
        for j in range(pos+1,l+1) :
            ans += dp[l][j]*j
        break
    else :
        ans += (10**(l -1-pos))*pos
        if pos == l-1 :
            ans += (10**(l -1-pos))*(pos+1)
    pos += 1
print(ans)

