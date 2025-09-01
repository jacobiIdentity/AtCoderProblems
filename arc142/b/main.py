#!/usr/bin/env python3
import numpy as np
n = int(input())
for i in range(1,n*n+1) :
    disp = n*n-i//2+1 if i%2 == 0 else (i+1)//2
    print(disp, end=("\n" if i%n==0 else " "))
