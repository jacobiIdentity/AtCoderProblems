#!/usr/bin/env python3
import math
from collections import deque
x, a, b  = map(int, input().split())
print('A' if abs(x-a) <= abs(x-b) else 'B')