#!/usr/bin/env python3
import itertools,math
s = input()
d = {'atcoder'[i]:i for i in range(7)}
visited = [0]*(math.factorial(7))
