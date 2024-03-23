from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    count = 0
    n, m = map(int, input().split())
    queue = deque(list(input().split()))

    while queue:
        max_point = max(queue)
        current = queue.popleft()

        if current == max_point:
            count += 1
            if m == 0:
                break
            else:
                m -= 1
        else:
            queue.append(current)
            if m == 0:
                m = len(queue) - 1
            else:
                m -= 1

    print(count)
