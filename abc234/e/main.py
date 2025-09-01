#!/usr/bin/env python3
import bisect
x = int(input())
an = list(range(1,100))
l = 3
while l<19 :
    a1 = 1
    while a1 < 10 :
        for d in range(-4,5) :
            if 0 <= a1+(l-1)*d<= 9 :
                digits = []
                tmp = a1
                while len(digits)<l and  0<= tmp < 10 :
                    digits.append(str(tmp))
                    tmp += d
                # if len(digits)==l :
                #     an.append(int(''.join(digits)))
                an.append(int(''.join(digits)))
        a1 += 1
    l += 1
# print(an)
print(an[bisect.bisect_left(an,x)])