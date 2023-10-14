# s = input()
# n_list = [-1 for i in range(26)]
# alpha_list = [chr(i + 97) for i in range(26)]

# for i in range(len(s)):
#     if n_list[alpha_list.index(s[i])] == -1:
#         n_list[alpha_list.index(s[i])] = i

# print(*n_list)

s = input()
alpha_list = [chr(i + 97) for i in range(26)]

for i in alpha_list:
    print(s.find(i), end=" ")
