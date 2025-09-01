#!/usr/bin/env python3
n = int(input())
a_n = list(map(int,input().split()))
evens = [a for a in a_n if a%2==0]
evens.sort()
odds = [a for a in a_n if a%2==1]
odds.sort()
ans = -1
if len(evens) > 1 :
    ans = max(ans,evens[-1]+evens[-2]) 
if len(odds) > 1 :
    ans = max(ans,odds[-1]+odds[-2])
print(ans)