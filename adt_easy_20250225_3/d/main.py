#!/usr/bin/env python3
xs = [int(s) for s in input()]
ans = 'Strong'
if xs[0]==xs[1]==xs[2]==xs[3] : ans = 'Weak'
if xs[1]%10==(xs[0]+1)%10 and xs[2]%10==(xs[0]+2)%10 and xs[3]%10==(xs[0]+3)%10 : ans = 'Weak'
print(ans)