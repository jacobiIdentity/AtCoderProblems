#!/usr/bin/env python3
a,b,c = map(int,input().split())
print('Yes' if c==a*b or b==c*a or a==b*c else 'No')