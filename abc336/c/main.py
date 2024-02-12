#!/usr/bin/env python3
n = int(input())
n -= 1
ans = ''
if n== 0 :
    print(n)
    exit()
while n > 0 :
    if n%5 == 0 :
        ans = '0'+ans
    if n%5 == 1 :
        ans = '2'+ans
    if n%5 == 2 :
        ans = '4'+ans
    if n%5 == 3 :
        ans = '6'+ans
    if n%5 == 4 :
        ans = '8'+ans
    n //= 5
print(ans)