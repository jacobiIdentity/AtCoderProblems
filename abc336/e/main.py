#!/usr/bin/env python3
n = int(input())
digitsLen = len(str(n))
perm = set()
for a01 in range(10) :
    if a01 <= digitsLen*9 :
        perm.add([a01])
    for a02 in range(a01,10) :
        if digitsLen < 2 :
            break
        if a01+a02 <= digitsLen*9 :
            perm.add([a01,a02])
        for a03 in range(a02,10) :
            if digitsLen < 3 :
                break
            if a01+a02+a03 <= digitsLen*9 :
                perm.add([a01,a02,a03])
            for a04 in range(a03,10) :
                if digitsLen < 4 :
                    break
                if a01+a02+a03+a04 <= digitsLen*9 :
                    perm.add([a01,a02,a03,a04])
                for a05 in range(a04,10) :
                    if digitsLen < 5 :
                        break
                    if a01+a02+a03+a04+a05 <= digitsLen*9 :
                        perm.add([a01,a02,a03,a04,a05])
                    for a06 in range(a05,10) :
                        if digitsLen < 6 :
                            break
                        if a01+a02+a03+a04+a05+a06 <= digitsLen*9 :
                            perm.add([a01,a02,a03,a04,a05,a06])
                        for a07 in range(a06,10) :
                            if digitsLen < 6 :
                                break
                            if a01+a02+a03+a04+a05+a06+a07 <= digitsLen*9 :
                                perm.add([a01,a02,a03,a04,a05,a06,a07])
                            for a07 in range(a06,10) :
                                if digitsLen < 6 :
                                    break
                                if a01+a02+a03+a04+a05+a06+a07 <= digitsLen*9 :
                                    perm.add([a01,a02,a03,a04,a05,a06,a07])

