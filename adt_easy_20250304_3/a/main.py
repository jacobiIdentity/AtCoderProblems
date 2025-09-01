#!/usr/bin/env python3
y = int(input())
ans = 366
if y%4>0 : ans = 365
elif y%400==0 : ans = 366
elif y%100==0 : ans = 365
print(ans)