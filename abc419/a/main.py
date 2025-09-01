#!/usr/bin/env python3
s = input()
d = dict()
d["red"] = "SSS"
d["blue"] = "FFF"
d["green"] = "MMM" 
if s in d :
    print(d[s])
else :
    print("Unknown")