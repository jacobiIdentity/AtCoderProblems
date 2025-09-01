#!/usr/bin/env python3
a,b,c,k = map(int,input().split())
print(min(a,k)+0*min(b,k-min(a,k))-min(c,k-min(a,k)-min(b,k-min(a,k))))