#!/usr/bin/env python3
s = input()
a,b='',''
for i in range(len(s)) :
    if s[i]=="#" :
        if a=='' :
            a=str(i+1)
        else :
            b=str(i+1)
            print(','.join([a,b]))
            a,b='',''
