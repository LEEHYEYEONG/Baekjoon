# 왜 안되는지 이유 찾기
# alpha_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

# num_word = 0
# new_list = []
# word = input()
# new_word = word[:]

# for i in range(len(alpha_list)):
#     if alpha_list[i] in new_word:
#         num_word += word.count(alpha_list[i])
#         word = word.replace(alpha_list[i], "")
#         new_list.append(word)

# if not new_list:
#     print(len(word))
# else:
#     print(len(new_list[-1]) + num_word)

alpha_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

for i in range(len(alpha_list)):
    if alpha_list[i] in word:
        word = word.replace(alpha_list[i], " ")
print(len(word))
