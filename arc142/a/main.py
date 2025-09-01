#!/usr/bin/env python3
import numpy as np
n = int(input())
f = {1,-1,n,-n}
i,tmp = 2, n
for i in range(2, int(n**0.5)+1) :
    if n%i == 0 :
        f |= {i,-i,n//i,-n//i}
# print(f)
for ff in f :
    ans = np.roots([5,10*ff,10*ff**2,5*ff**3,ff**4 - n//ff ])
    # print(ans)
    for bb in ans :
        if np.isreal(bb) and np.isclose(bb.imag,0) :
            b = int(round(bb.real))
            if (b+ff)**5 - b**5 == n :
                print(b+ff, b)
                exit()
            if (b+ff+1)**5 - (b+1)**5 == n :
                print(b+1+ff, b+1)
                exit()
            if (b+ff-1)**5 - (b-1)**5 == n :
                print(b-1+ff, b-1)
                exit()
