import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque([i + 1 for i in range(n)])

for i in range(n - 1):
    queue.popleft()
    tmp = queue.popleft()
    # queue.insert(len(queue), tmp)
    queue.append(tmp)

print(queue[0])
