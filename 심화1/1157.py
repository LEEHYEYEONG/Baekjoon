# word = input()

# alph_list = [0 for _ in range(26)]

# for i in range(len(word)):
#     alph_list[ord(word[i].upper()) - 65] += 1

# index_list = [i for i, value in enumerate(alph_list) if value == max(alph_list)]

# if len(index_list) == 1:
#     print(chr(index_list[0] + 65))
# else:
#     print("?")

word = input().upper()

set_word = list(set(word))
count_list = []

for i in set_word:
    count_list.append(word.count(i))

if count_list.count(max(count_list)) > 1:
    print("?")
else:
    print(set_word[count_list.index(max(count_list))])
