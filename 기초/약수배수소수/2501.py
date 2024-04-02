n, k = map(int, input().split())
n_list = []

for i in range(1, n + 1):
    if n % i == 0:
        n_list.append(i)

if len(n_list) >= k:
    print(n_list[k - 1])
else:
    print(0)

# N, K = map(int, input().split())

# result = 0

# for i in range(1, N + 1):
#     if N % i == 0:
#         K -= 1
#         if K == 0:
#             result = i
#             break

# print(result)
