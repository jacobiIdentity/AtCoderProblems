#!/usr/bin/env python3
n,m = map(int,input().split())
biM = format(f'{m:060b}')
# print(biM)
ans = 0
for i in range(60) :
    if biM[59-i] == '1':
        ans += (n//(2**(i+1)))*(2**i)
        ans %= 998244353
        ans += max(0,(n%(2**(i+1)))-(2**i)+1)
        ans %= 998244353
print(ans)