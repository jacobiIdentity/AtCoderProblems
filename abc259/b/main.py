#!/usr/bin/env python3
import math
a,b,d = map(int,input().split())
print(a*math.cos(d*math.pi/180)-b*math.sin(d*math.pi/180),a*math.sin(d*math.pi/180)+b*math.cos(d*math.pi/180))