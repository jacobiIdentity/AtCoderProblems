#!/usr/bin/env python3
a_n = list(map(int,input().split()))
geq3,eq2 = set(),set()
for i in range(7) :
    if a_n.count(a_n[i]) > 2 :
        geq3.add(a_n[i])
    elif a_n.count(a_n[i]) == 2 :
        eq2.add(a_n[i])
if len(geq3)>=2 or (len(geq3)==1 and len(eq2)>=1) :
    print('Yes')
else:
    print('No')
        

    