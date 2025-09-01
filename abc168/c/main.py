#!/usr/bin/env python3
from math import pi,cos,sqrt
a,b,h,m = map(int,input().split())
theta_base = abs(12*m-60*h-m)
# if theta_base >= 180 :
#     theta_base = 360-theta_base
print(sqrt(a*a+b*b-2*a*b*cos(theta_base*pi/360)))