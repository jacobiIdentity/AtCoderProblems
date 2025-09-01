#!/usr/bin/env python3
from collections import defaultdict,deque
n,m,k = map(int,input().split())
a_n = list(map(int,input().split()))
threshold = k -sum(a_n)