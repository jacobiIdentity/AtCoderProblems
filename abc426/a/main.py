#!/usr/bin/env python3
version = {"Ocelot":0, "Serval":1, "Lynx":2}
x,y = input().split()
print('YNeos'[version[y]-version[x]>0 ::2])