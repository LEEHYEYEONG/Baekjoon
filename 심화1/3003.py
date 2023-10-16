n_list = [int(n) for n in input().split()]
right_list = [1, 1, 2, 2, 2, 8]

for i in range(len(n_list)):
	n_list[i] = right_list[i] - n_list[i]

print(*n_list)