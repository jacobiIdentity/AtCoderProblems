#!/usr/bin/env python3
n = int(input())
ans = 0
for i in range(1,len(str(n))) :
    ans += ((pow(10,i,998244353)-pow(10,i-1,998244353))*(pow(10,i,998244353)-pow(10,i-1,998244353)+1))//2
    ans %= 998244353
ans += ((n-pow(10,len(str(n))-1,998244353)+1)*(n-pow(10,len(str(n))-1,998244353)+2))//2
ans %= 998244353
print(ans)