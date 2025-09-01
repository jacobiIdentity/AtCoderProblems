#!/usr/bin/env python3
from math import cos,sin,pi
n = int(input())
x0,y0 = map(int,input().split())
xn_2,yn_2 = map(int,input().split())
xbase,ybase = x0-xn_2,y0-yn_2
xOrig,yOrig = x0+xn_2,y0+yn_2
print((xbase*cos(2*pi/n)-ybase*sin(2*pi/n)+xOrig)/2,(xbase*sin(2*pi/n)+ybase*cos(2*pi/n)+yOrig)/2)
