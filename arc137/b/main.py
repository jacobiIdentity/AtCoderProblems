#!/usr/bin/env python3
import itertools
n = int(input())
a_n = list(map(int,input().split()))
acs = [0]+list(itertools.accumulate(a_n))
left,right = 0,0
ans = {acs[-1]}
cnt1,cnt0 = 0,0
while right<n :
    cnt1 += a_n[right]
    cnt0 += 1-a_n[right]
    # print(left,right,cnt0,cnt1,acs[-1]-acs[right+1]+cnt0+acs[left]-acs[0])
    ans.add(acs[-1]-acs[right+1]+cnt0+acs[left]-acs[0])
    if cnt1 == cnt0 :
        # while right-left>0 :
            cnt1 -= a_n[left]
            cnt0 -= 1-a_n[left]
            ans.add(acs[-1]-acs[right+1]+cnt0+acs[left]-acs[0])
            left += 1
            continue
            # print(left,right,cnt0,cnt1,acs[-1]-acs[right+1]+cnt0+acs[left]-acs[0])
        # left += 1
    right +=1
print(len(ans))
# def max_subarray_sum(arr):
#     max_sum = float('-inf')
#     current = 0
#     for x in arr:
#         current = max(x, current + x)
#         max_sum = max(max_sum, current)
#     return max_sum

# def min_subarray_sum(arr):
#     min_sum = float('inf')
#     current = 0
#     for x in arr:
#         current = min(x, current + x)
#         min_sum = min(min_sum, current)
#     return min_sum

# n = int(input())
# A = list(map(int, input().split()))

# original_ones = sum(A)

# # 各要素を 0 -> +1, 1 -> -1 に変換
# delta = [1 if a == 0 else -1 for a in A]

# max_gain = max(0, max_subarray_sum(delta))  # 空部分列も含む（操作なし＝0）
# min_gain = min(0, min_subarray_sum(delta))

# # スコアは original_ones + [min_gain, ..., max_gain] の整数範囲
# print(max_gain - min_gain + 1)