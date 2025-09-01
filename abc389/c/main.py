#!/usr/bin/env python3
q = int(input())
top = 0
length = 0
snakes = []
cms = [0]
for _ in range(q) :
    query = input()
    if query[0] == '1' :
        snakes.append(int(query[2:]))
        # if len(cms) == 0 :
        #     cms.append(snakes[-1])
        # else :
            # cms.append(snakes[-1]+cms[-1])
        cms.append(snakes[-1]+cms[-1])
    elif query[0] == '2' :
        length += snakes[top]
        top += 1
    else :
        print(cms[int(query[2:])-1+top]-cms[top])
# print(snakes)
# print(cms)
