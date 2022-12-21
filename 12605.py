#단어 순서

import sys

input = sys.stdin.readline

case=int(input())

k=[list(map(str,input().split())) for _ in range(case)]

for i in range(case):
    res = []
    a=len(k[i])
    for j in range(a):
        res.append(k[i].pop())
    print('Case #{0}: {1}'.format(i+1,' '.join(res)))
