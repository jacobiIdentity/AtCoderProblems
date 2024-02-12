from collections import defaultdict
n = int(input())
q = int(input())
box = defaultdict(list)
card = defaultdict(set)
for _ in range(q) :
    query = input()
    if query[0] == '1' :
        q, i, j = map(int, query.split())
        box[j].append(i)
        if j not in card[i] :
            card[i].add(j)
    elif query[0] == '2' :
        q, i = map(int, query.split())
        print(*sorted(box[i]))
    else :
        q, i = map(int, query.split())
        print(*sorted(list(card[i])))
