import sys
from math import gcd, sqrt

input = sys.stdin.readline

n = int(input())
answer = []


# 라이브러리 사용 x
def calc_gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a %= b
        a, b = b, a

    return a


# gcd를 이용해서 최대공약수
if n == 2:
    a, b = map(int, input().split())
    gcd_num = gcd(a, b)

else:
    a, b, c = map(int, input().split())
    gcd_num = gcd(gcd(a, b), c)

for i in range(1, int(sqrt(gcd_num)) + 1):
    print(i)
    if gcd_num % i == 0:
        answer.append(i)
        if i**2 != gcd_num:
            answer.append(gcd_num // i)

answer.sort()

for i in answer:
    print(i)
