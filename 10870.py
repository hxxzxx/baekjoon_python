#피보나치

import sys

input = sys.stdin.readline

a= int(input())

def fibo(a):
    if( a > 1):
        return fibo(a-1)+fibo(a-2)
    elif (a == 0):
        return 0
    elif (a == 1):
        return 1
print(fibo(a))