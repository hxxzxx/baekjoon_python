#더하기 사이클

import sys
input = sys.stdin.readline

n = int(input())
original = n
count = 0
while(1):
    new_a = ((n // 10) + (n % 10))%10
    n = new_a + (n%10)*10
    count+=1
    if(n == original):
        print(count)
        break;