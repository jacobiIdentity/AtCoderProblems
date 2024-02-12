#!/usr/bin/env python3
import math
from collections import deque
a, b = map(int, input().split())
a, b = (b, a) if a > b else (a, b)
if a * 2*(3**0.5)/3 < b :
    print('{:.16f}'.format(a * 2/(3**0.5)))
else :
    print('{:.16f}'.format(a / math.cos(math.atan(2*b/a-3**0.5))))