#!/usr/bin/env python3
n = int(input())
s = input()
ans = ''
if n%2 == 0 :
    print('No')
    exit()
elif  '1'*((n+1)//2-1) + '/' + '2'*((n+1)//2-1)== s :
    print('Yes')
else :
    print('No')
# print('1'*((n+1)//2) + '/' + '2'*((n+1)//2))
# print(s)
