#!/usr/bin/env python3
grid = [input() for _ in range(2)]
print('No' if (grid == ['#.','.#']) or (grid == ['.#','#.']) else 'Yes')