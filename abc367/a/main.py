#!/usr/bin/env python3
a,b,c = map(int,input().split())
print('Yes' if (b<c and (c<a or a<b)) or (c<a<b ) else 'No')