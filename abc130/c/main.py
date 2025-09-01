#!/usr/bin/env python3
w,h,x,y = list(map(int,input().split()))
print(w*h/2,(1 if x*2==w and y*2==h else 0))