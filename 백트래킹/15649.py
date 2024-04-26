import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
num_list = [i + 1 for i in range(n)]

pick = list(permutations(num_list, m))

for i in pick:
    print(*i)
