# n_num = int(input())
# n = int(input())
# sum = 0

# for i in range(n_num):
#     sum += n % 10
#     n = n // 10

# print(sum)

n_num = int(input())
n = input()
sum = 0

for i in range(n_num):
    sum += int(n[i])

print(sum)
