#!/usr/bin/env python3
v1,v2,v3 = map(int,input().split())
for a2 in range(-7,8) :
    for b2 in range(-7,8) :
        for c2 in range(-7,8) :
            for a3 in range(8) :
                for b3 in range(8) :
                    for c3 in range(8) :
                        v_123 = max(0,min(0,a2,a3)+7-max(0,a2,a3))*max(0,min(0,b2,b3)+7-max(0,b2,b3))*max(0,min(0,c2,c3)+7-max(0,c2,c3))
                        v_12  = max(0,max(0,(min(0,a2)+7-max(0,a2)))*max(0,min(0,b2)+7-max(0,b2))*max(0,min(0,c2)+7-max(0,c2))-v_123)
                        v_13  = max(0,max(0,(min(0,a3)+7-max(0,a3)))*max(0,min(0,b3)+7-max(0,b3))*max(0,min(0,c3)+7-max(0,c3))-v_123)
                        v_23  = max(0,max(0,(min(a2,a3)+7-max(a2,a3)))*max(0,min(b2,b3)+7-max(b2,b3))*max(0,min(c2,c3)+7-max(c2,c3))-v_123)
                        v_1   = 343 - v_12 - v_13 + v_123
                        v_2   = 343 - v_12 - v_23 + v_123
                        v_3   = 343 - v_13 - v_13 + v_123
                        if v1 == v_1+v_2+v_3 and v2 == v_12+v_13+v_23 and v3 == v_123 :
                            print("Yes")
                            print(0,0,0,a2,b2,c2,a3,b3,c3)
                            exit()
print("No")
