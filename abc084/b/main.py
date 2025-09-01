#!/usr/bin/env python3
a,b = map(int,input().split())
s = input()
print('YNeos'[not(s[:a].isdigit() and s[a]=="-" and s[a+1:].isdigit())::2])