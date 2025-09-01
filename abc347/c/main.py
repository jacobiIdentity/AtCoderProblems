#!/usr/bin/env python3
n,a,b = map(int,input().split())
d = set(map(lambda x:(int(x)-1)%(a+b),input().split()))
# print(d)
d = list(d)
d.sort()
days = max(d)-min(d)+1
if len(d)> 1:
    days = min(days,d[0]+1+a+b-d[1])
# for i in range(len(d)-1) :
#     days = min(days,d[i]+1+a+b-d[i+1])
print('YNeos'[days>a::2])

