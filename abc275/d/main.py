#!/usr/bin/env python3
from functools import lru_cache


@lru_cache
def f(n):
    if n == 0:
        return 1
    return f(n // 2) + f(n // 3)


print(f(int(input())))

# import sys
# import resource
def f(x) :
    if x == 0 :
        return 1
    else :
        return f(x//2)+f(x//3)
    # if fval[x] != float('inf') :
    #     return
    # if fval[x//2] == float('inf') :
    #     f(x//2)
    # if fval[x//3] == float('inf') :
    #     f(x//3)
    # fval[x] = fval[x//2] + fval[x//3]
    # return
# resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))
# print(resource.getrlimit(resource.RLIMIT_STACK))
# sys.setrecursionlimit(10**9)
# n = int(input())
# fval = [float('inf')]*(n+1)
# fval[0] = 1
# f(n)
# print(f(n))
# print(fval[n])
# print(fval)


