#!/usr/bin/env python3
n = int(input())
ans = 0
digit = 1
while digit < len(str(n)) :
    ans += 10**digit-10**(digit-1)
    # ans += ((10**digit-10**(digit-1))*(10**digit+10**(digit-1)-1))//2
    digit += 2
if len(str(n))%2 :
    ans += (n - 10**(digit-1)+1)
    # ans += ((n - 10**(digit-1)+1)*(n + 10**(digit-1)))//2

print(ans)
