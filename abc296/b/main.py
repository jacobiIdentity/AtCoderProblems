#!/usr/bin/env python3
board = [input() for i in range(8)]
endFlg = False
for i in range(8) :
    for j in range(8) :
        if board[i][j] == '*' :
            print(chr(ord('a')+j)+str(8-i))

