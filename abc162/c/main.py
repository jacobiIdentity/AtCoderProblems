#!/usr/bin/env python3
def getDiv(x) :
    divs = set()
    tmp = 1
    while tmp*tmp <= x :
        if x%tmp == 0 :
            divs.add(x//tmp)
            divs.add(tmp)
        tmp += 1
    return divs
def gcm(divs,gcms) :
    ret = 1
    for d in divs :
        isYes = True
        for x in gcms :
            if x%d > 0 :
                isYes = False
        if isYes :
            ret = max(ret,d)
    return ret

k = int(input())
ans = 0
for a in range(1,k+1) :
    ans += a
    # print(a)
    for b in range(a+1,k+1) :
        ans += gcm(getDiv(a),[a,b])*6
        # print(a,b,gcm(getDiv(a),[a,b]))
        for c in range(b+1,k+1) :
            # print(a,b,c,gcm(getDiv(a),[a,b,c]))
            ans += gcm(getDiv(a),[a,b,c])*6
print(ans)
