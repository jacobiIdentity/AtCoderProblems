#!/usr/bin/env python3
def rotate(x) :
    rotate_x = [["."]*4 for _ in range(4)]
    for h in range(4) :
        for w in range(4) :
            rotate_x[w][3-h] = x[h][w]
    return rotate_x
def firstRow(x) :
    for h in range(4):
        for w in range(4):
            if x[h][w]=="#":
                return h
def firstCol(x) :
    for w in range(4):
        for h in range(4):
            if x[h][w]=="#":
                return w

p144 = [list(input()) for _ in range(4)]
p244 = [list(input()) for _ in range(4)]
p344 = [list(input()) for _ in range(4)]

for i in range(4) :
    p144 = rotate(p144)
    i1,i2 = firstRow(p144),firstCol(p144)
    print(p144,i1,i2)
    for j in range(4) :
        p244 = rotate(p244)
        j1,j2 = firstRow(p244),firstCol(p244)
        print(p244,j1,j2)
        for k in range(4) :
            p344 = rotate(p344)
            k1,k2 = firstRow(p344),firstCol(p344)
            print(p344,k1,k2)
            for l1 in range(4) :
                if l1 + i1 > 3 :
                    break
                for l2 in range(4) :
                    if l2 + i2 > 3 :
                        break
                    for m1 in range(4) :
                        if m1 + j1 > 3 :
                            break
                        for m2 in range(4) :
                            if m2 + j2 > 3 :
                                break
                            for n1 in range(4) :
                                if n1 + k1 > 3 :
                                    break
                                for n2 in range(4) :
                                    if n2 + k2 > 3 :
                                        break
                                    isOK = True
                                    for h in range(4) :
                                        for w in range(4) :
                                            p1 = (p144[h][w] == '#')
                                            p2 = (p244[h][w] == '#')
                                            p3 = (p344[h][w] == '#')
                                            if p1 and not(p2) and not(p3) :
                                                print('Yes')
                                                exit()
                                            if not(p1) and p2 and not(p3) :
                                                print('Yes')
                                                exit()
                                            if not(p1) and not(p2) and p3 :
                                                print('Yes')
                                                exit()
                                            isOK = False
                                            break
                                    if not(isOK) :
                                        break
print('No')
