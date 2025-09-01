#!/usr/bin/env python3
x = input()
while True :
    if (x[-1] == '0' and x.find('.') != -1) or x[-1]=='.' :
        x = x[:-1]
    else :
        break
print(x)