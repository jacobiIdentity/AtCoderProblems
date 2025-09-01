#!/usr/bin/env python3
x,y = map(int,input().split())
print('YNeos'[max(x,y)-min(x,y)-3>=0::2])