#!/usr/bin/env python3
a,b,c = map(int,input().split())
print('Yes' if a==(b+c) or b==(c+a) or c==(a+b) else 'No')