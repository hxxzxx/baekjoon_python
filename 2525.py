#import sys

#input = sys.stdin.readline

h,m = input().split()
h=int(h)
m=int(m)
p = int(input())
m=m+p
while(1):
    if(m < 60):
        break
    elif(m>=60):
        h=h+(m//60)
        m=m%60
        h=h%24
print(h,m)