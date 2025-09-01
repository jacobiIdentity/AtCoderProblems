#!/usr/bin/env python3
from collections import defaultdict

t = int(input())
for _ in range(t) :
    a_n = list(map(int,input().split()))
    p_n = list(map(int,input().split()))
    pts = -(2*a_n[4]+a_n[3]-a_n[1]-2*a_n[0])
    print(max(0,min(pts*p_n[3],(pts//2)*p_n[4]+(pts%2)*min(p_n[4],p_n[3]))))
    # if pts <= 0 :
    #     print(0)
    # else :
    #     print(min(pts*p_n[3],(pts//2)*p_n[4]+(pts%2)*min(p_n[4],p_n[3])))