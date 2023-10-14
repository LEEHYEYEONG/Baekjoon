remainder_list = list()
for i in range(10):
	n = int(input())
	remainder = n % 42
	remainder_list.append(remainder)

print(len(set(remainder_list)))