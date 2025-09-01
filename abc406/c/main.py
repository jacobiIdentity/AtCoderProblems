#!/usr/bin/env python3
n = int(input())
p_n = list(map(int,input().split()))
tld = [0]
sign = p_n[1]-p_n[0]
for i in range(n-1) :
    if (p_n[i+1]-p_n[i])*sign < 0 :
        tld.append(i)
        sign *= -1
if len(tld) < 3 :
    print(0)
    exit()
tld.append(n-1)
# print(tld)
ans = 0
for i in range((p_n[1]-p_n[0]<0),len(tld)-3,2):
    ans += (tld[i+3]-tld[i+2])*(tld[i+1]-tld[i])
    # print((tld[i+3]-tld[i+2])*(tld[i+1]-tld[i]))
print(ans)