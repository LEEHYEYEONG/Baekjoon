import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for i in range(T):
    count = 0
    queue = deque(list(input().strip()))
    if queue[-1] == "(":
        print("NO")
    else:
        while queue:
            string = queue.pop()
            if string == ")":
                count += 1
            elif string == "(":
                count -= 1

            if count < 0:
                break

        if count == 0:
            print("YES")
        else:
            print("NO")
