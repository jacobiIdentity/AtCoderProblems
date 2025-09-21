#!/usr/bin/env python3
a,b,c = map(int,input().split())
if a==b or b==c or c==a :
    print('Yes')
else :
    print('No')