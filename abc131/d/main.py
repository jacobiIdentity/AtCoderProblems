#!/usr/bin/env python3
from collections import defaultdict
import sys
def merge(data, s, m, e) :
    tmp = []
    i = s
    j = m+1
    while i <= m and j <= e :
        if data[i][1] < data[j][1] :
            tmp.append(data[i])
            i += 1
        else :
            tmp.append(data[j])
            j += 1
    while i <= m :
        tmp.append(data[i])
        i += 1
    while j <= e :
        tmp.append(data[j])
        j += 1
    k = s
    for d in tmp :
        data[k] = d
        k += 1
def merge_sort(data, s, e) :
    if s >= e : return
    m = (s+e)//2
    merge_sort(data, s, m)
    merge_sort(data, m+1, e)
    merge(data, s, m, e)



todoList = []
n = int(input())
for _ in range(n) :
    a, b = map(int, input().split())
    todoList.append((a,b))
merge_sort(todoList, 0, n-1)
# print(todoList)
now = 0
for (a,b) in todoList :
    now += a
    if now > b :
        print('No')
        exit()
print('Yes')