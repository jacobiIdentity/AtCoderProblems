#!/usr/bin/env python3
from collections import defaultdict
n,k = map(int,input().split())
s = list(input())
for i in range(n) :
    if s[i]=='o' and 0<=i+1<n and s[i+1]=='?' :
        s[i+1] = '.'
    if s[i]=='o' and 0<=i-1<n and s[i-1]=='?' :
        s[i-1] = '.'
# print(s)
d1 = defaultdict(int)
d2 = defaultdict(int)
left = 0
while left < n :
    if s[left] == '?' :
        right = left
        while right<n :
            if s[right] != '?' :
                break
            right += 1
        d1[right-left] += 1
        d2[left] = right-left
        left = right
    else :
        left += 1
# print(d1)
# print(d2)
tmp = 0
for i in d1 :
    tmp += d1[i]* (i//2+i%2)
# print(tmp)
if s.count('o')==k :
    print(''.join(s).replace('?','.'))
    exit()
isFull =  tmp+s.count('o') <= k
for i in d2 :
    if d2[i]%2==1 and isFull :
        for j in range(d2[i]) :
            s[i+j] = 'o' if j%2==0 else '.'
print(''.join(s))