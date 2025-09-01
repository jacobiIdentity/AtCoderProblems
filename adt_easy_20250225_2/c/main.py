#!/usr/bin/env python3
a,b,c,d = 0,10,0,10
for i in range(10) :
    s = input()
    if s.find('#') > -1 :
        if a == 0 :
            a= i+1
        if c == 0 :
            c= s.find('#')+1
        # ↓初期値b=10にしておけば不要
        # if i == 9 :
            # b=i+1
    elif a>0 and b==10 :
        b = i
    if s.rfind('#') > -1 :
        if d==10 :
            d=s.rfind('#')+1
print(a,b)
print(c,d)