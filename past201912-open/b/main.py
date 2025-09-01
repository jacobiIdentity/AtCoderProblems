#!/usr/bin/env python3
n = int(input())
a_n = [int(input()) for _ in range(n)]
acs = []
for i in range(n-1) :
    acs.append(a_n[i+1]-a_n[i])
# print(acs)
for i in range(n-1) :
    if acs[i] == 0 :
        print("stay")
    elif acs[i]>0 :
        print("up", str(acs[i]))
    else :
        print("down", str(abs(acs[i])))

