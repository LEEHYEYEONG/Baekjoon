n = int(input())
group = 0
for i in range(n):
	word = input()
	same_list = []
	same = False
	for j in range(len(word)):
		if(word[j] in same_list):
			same = True
			break
		if((j != len(word)-1) and word[j] != word[j+1]):
			same_list.append(word[j])
	if same == False:
		group += 1

print(group)

# result = 0
# for i in range(int(input())):
#     word = input()
#     if list(word) == sorted(word, key=word.find):
#         print(list(word))
#         print(sorted(word, key=word.find))
#         result += 1
# print(result)