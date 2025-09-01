#!/usr/bin/env python3
import sys
import itertools
import bisect

# 標準入力を高速に処理する
input = sys.stdin.read
data = input().split()

n = int(data[0])
x_n = list(map(int, data[1:n+1]))
p_n = list(map(int, data[n+1:2*n+1]))
cms = list(itertools.accumulate(p_n))

q = int(data[2*n+1])
queries = data[2*n+2:]

# クエリ処理
result = []
for i in range(q):
    l = int(queries[2*i])
    r = int(queries[2*i+1])
    
    if r < x_n[0] or l > x_n[-1]:
        result.append(0)
        continue
    
    # 二分探索で範囲の左と右を取得
    lx = bisect.bisect_left(x_n, l)
    rx = bisect.bisect_right(x_n, r) - 1

    if lx == len(x_n) or x_n[lx] > r:
        result.append(0)
        continue
    
    B = cms[rx] if rx >= 0 else 0
    S = cms[lx-1] if lx > 0 else 0
    
    result.append(max(0, B - S))

# 一度に出力する
sys.stdout.write("\n".join(map(str, result)) + "\n")

# import itertools,bisect
# n = int(input())
# x_n =list(map(int,input().split()))
# p_n =list(map(int,input().split()))
# cms = list(itertools.accumulate(p_n))
# # print(cms)
# q = int(input())
# for _ in range(q) :
#     l,r =map(int,input().split())
#     if r < x_n[0] or  l > x_n[-1] :
#         print(0)
#         continue    
#     lx = bisect.bisect_left(x_n,l)
#     rx = bisect.bisect_left(x_n,r)
#     # print(lx,rx)
#     B,S = 0,0
#     if r not in x_n and rx > 0 :
#         rx -= 1
#     B = cms[rx]
#     if lx == 0 :
#         S = 0
#     else :
#         S = cms[lx-1]
#     # print(lx,rx,S,B)
#     print(max(0,B-S))
# import sys, bisect

# def main():
#     import sys
#     from bisect import bisect_left

#     data = sys.stdin.read().split()
#     ptr = 0

#     n = int(data[ptr])
#     ptr +=1

#     x_n = list(map(int, data[ptr:ptr+n]))
#     ptr +=n

#     p_n = list(map(int, data[ptr:ptr+n]))
#     ptr +=n

#     # 累積和の計算
#     cms = [0]*n
#     cms[0] = p_n[0]
#     for i in range(1,n):
#         cms[i] = cms[i-1] + p_n[i]

#     q = int(data[ptr])
#     ptr +=1

#     output = []
#     for _ in range(q):
#         l = int(data[ptr])
#         r = int(data[ptr+1])
#         ptr +=2

#         if r < x_n[0] or l > x_n[-1]:
#             output.append('0\n')
#             continue

#         lx = bisect_left(x_n, l)
#         rx = bisect_left(x_n, r)

#         if rx < n and x_n[rx] == r:
#             pass
#         else:
#             rx -=1

#         if rx < 0:
#             output.append('0\n')
#             continue

#         B = cms[rx]
#         S = cms[lx-1] if lx >0 else 0
#         res = B - S
#         if res <0:
#             res =0
#         output.append(str(res)+'\n')

#     sys.stdout.write(''.join(output))

# if __name__ == "__main__":
#     main()
