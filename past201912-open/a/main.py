#!/usr/bin/env python3
s = input()
for ss in s :
    if not(ss.isdigit()) :
        print("error")
        exit()
print(int(s)*2)