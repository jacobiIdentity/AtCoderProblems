#!/usr/bin/env python3
def checkBlack(R,C) :
    DISTANCE = max(abs(R-8),abs(C-8))
    isBlack = True if DISTANCE%2==1 else False
    return (isBlack, DISTANCE)

r,c = map(int ,input().split())
print('black'if checkBlack(r,c)[0] else 'white')
# for i in range(1,16) :
#     for j in range(1,16) :
#         flg, dist = checkBlack(i,j)
#         print(i,j,dist,'black'if flg else 'white')
