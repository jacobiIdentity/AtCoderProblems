#!/usr/bin/env python3
a,b,c,d = map(int,input().split())
if (a==b==c and d != a) \
or (b==c==d and a != b) \
or (c==d==a and b != c) \
or (d==a==b and b != c) \
or (a==b and c==d and a!=c)\
or (a==c and b==d and a!=b)\
or (a==d and b==c and a!=b) :
    print('Yes')
else :
    print('No')
