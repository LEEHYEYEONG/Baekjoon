from collections import deque
import sys

n, m = map(int, input().split())

way = 0

graph = []

for i in range(n):
    line = map(int, sys.stdin.readline().strip())
    graph.append(list(line))

need_visited = deque()
need_visited.append((0, 0))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while need_visited:
    x, y = need_visited.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                need_visited.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

print(graph[n - 1][m - 1])
