#!/usr/bin/env python3
def gcd(x,y) :
    if x>y : x,y =y,x
    if y%x==0 :
        return x
    else :
        return gcd(x,y%x)
a,b = map(int,input().split())
g = gcd(a,b)
ans = {1}
i = 2
while i*i <= g :
    if g%i==0 :
        while g%i==0 :
            g//=i
        ans.add(i)
    i+=1
if g>1 :
    ans.add(g)
print(len(ans))