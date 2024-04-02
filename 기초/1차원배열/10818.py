# n = int(input())
# n_list = [int(n) for n in input().split()]
# n_list = list(map(int, input().split()))

# n_min = n_list[0]
# n_max = n_list[0]

# for i in range(1, n):
# 	if(n_min > n_list[i]):
# 		n_min = n_list[i]
# 	elif(n_max < n_list[i]):
# 		n_max = n_list[i]

# print(n_min, n_max)

n = int(input())
n_list = [int(n) for n in input().split()]

print(min(n_list), max(n_list))