#!/usr/bin/env python3
x,y = map(int,input().split())
print((max(y-x,0))//10 + (1 if (max(y-x,0))%10 else 0))