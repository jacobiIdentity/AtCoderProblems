#!/usr/bin/env python3
import itertools
n = int(input())
s = input()
arr = []
for i in range(n) :
    if s[i] == '1' :
        arr.append(i)
acs = [0]+list(itertools.accumulate(arr))
ans = float('inf')
l = len(arr)
for i in range(l) :
    ans = min(ans,\
              acs[l]-acs[i+1]-arr[i]*(l-i-1)-((l-i-1)*(i+l)//2-i*(l-i-1)) \
              +abs(acs[i]-acs[0] -arr[i]*i)-abs(i*(i-1)//2-i*i))
    # print(acs[l]-acs[i+1],arr[i]*(l-i-1),((l-i-1)*(i+l)//2-i*(l-i-1)),acs[i+1]-acs[1],arr[i]*i,abs(i*(i-1)//2-i*i)) 
print(ans)
    
    