#!/usr/bin/env python3
import sys
from fractions import Fraction
n = int(input())
dots = [list(map(int, input().split())) for _ in range(n) ]
slope = [set() for _ in range(n) ]
for i in range(n) :
  for j in range(n) :
    if i == j : continue
    if dots[j][0]-dots[i][0] == 0 :
      slope[i].add("infinty")
    else :
      slope[i].add(Fraction(dots[j][1]-dots[i][1], dots[j][0]-dots[i][0]))

for i in range(len(slope)) :
  if len(slope[i]) != n-1 :
    print('Yes')
    exit()
print('No')