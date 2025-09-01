#!/usr/bin/env python3
# hits = set()
# for _ in range(4) :
#     hits.add(input())
# print('Yes' if len(hits) == 4 else 'No')
print('Yes' if len({input() for _ in range(4)}) == 4 else 'No')
