#!/usr/bin/env python3
m = int(input())
ans = []
for _ in range(20) :
    tmp = 10
    while tmp>=0 :
        if m//(3**tmp) > 0 :
            m -= 3**tmp
            ans.append(tmp)
            break
        elif m== 0 :
            break
        elif tmp == 0:
            m -= 1
            break
        else :
            tmp -= 1
    if m == 0 :
        break
print(len(ans))
print(*ans)


