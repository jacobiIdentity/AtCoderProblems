#!/usr/bin/env python3
a,b = map(int,input().split())
if (a//b+1)*b - a > a-(a//b)*b :
    print(a//b)
else :
    print(a//b+1)
