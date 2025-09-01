#!/usr/bin/env python3
r = int(input())
if r < 100 :
    print(100-r)
elif r < 200 :
    print(200-r)
else :
    print(300-r)
# print((100-r+1)%100-1)