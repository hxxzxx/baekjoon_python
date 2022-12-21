#막대기
import sys

input = sys.stdin.readline
a=[]
cnt=1

n = int(input())
a= [int(input()) for _ in range(n)]

max =a.pop() #맨마지막 요소

for i in range(n-1):
    m=a.pop()
    if(max < m):
        cnt+=1
        max=m

print(cnt)
