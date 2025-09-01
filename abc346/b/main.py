#!/usr/bin/env python3
w,b = map(int, input().split())
while True :
    if not(w//7 >= 1 and b//5 >= 1) :
        break
    w -= 7
    b -= 5
keyBoard = 'wbwbwwbwbwbw'*2
isOKs = set()
for i in range(len(keyBoard)) :
    for j in range(i,len(keyBoard)+1) :
        isOKs.add((keyBoard[i:j].count('w'),keyBoard[i:j].count('b')))
print('Yes' if (w,b) in isOKs else 'No')