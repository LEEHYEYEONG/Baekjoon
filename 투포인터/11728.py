import sys
import heapq

# 내가 생각한 풀이

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = a + b
result.sort()

print(*result)


# 힙 정렬

input = sys.stdin.readline

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

heapq.heapify(a)

for i in range(m):
    heapq.heappush(a, b[i])

for i in range(n + m):
    print(heapq.heappop(a), end=" ")


# 투포인터

n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = []

a, b = 0, 0
while a != len(A) or b != len(B):
    if a == len(A):
        result.append(B[b])
        b += 1
    elif b == len(B):
        result.append(A[a])
        a += 1
    else:
        if A[a] < B[b]:
            result.append(A[a])
            a += 1
        else:
            result.append(B[b])
            b += 1

print(*result)
