#!/usr/bin/env python3
a_n = input()
ans = 0
for i in range(1,5) :
    ans += a_n.count(str(i))//2
    # print(i,a_n.count(str(i)))
print(ans)
