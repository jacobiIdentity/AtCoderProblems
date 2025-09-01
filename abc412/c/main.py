#!/usr/bin/env python3
import heapq
t = int(input())
for _ in range(t) :
    n = int(input())
    s_n = list(map(int,input().split()))
    s0,sl = s_n[0],s_n[-1]
    if sl - s0*2<=0 :
        print(2)
        continue
    heap = []
    for i in range(1,n-1) :
        heapq.heappush(heap,s_n[i])
    m,prev,ans,isEnd = s0,-1,2,False
    # print(heap)
    d = [s0]
    while heap :
        now = heapq.heappop(heap)
        
        # print(d)
        # print(now,prev,ans,isEnd)
        if sl-now*2<=0 : #最後のドミノを倒せる
            d.append(now)
            print(len(d)+1)
            isEnd=True
            break
        elif now-m*2>0 :  #並べ済のドミノの一番最後から倒せない
            if prev==-1 : #前のドミノがない
                prev(-1)
                isEnd = True
                break
            ans += 1
            m,prev = prev,now #prevを並べ済最後のドミノにする
            d.append(m)

        else : #今のドミノから倒せる
            prev = now
    if not(isEnd) :
        print(-1)