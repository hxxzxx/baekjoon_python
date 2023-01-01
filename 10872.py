#팩토리얼

import sys

input = sys.stdin.readline

a=int(input())

def facto(a):
    if a > 1:
        return a * facto(a - 1)
    else:
        return 1

print(facto(a))