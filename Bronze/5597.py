students = [int(input()) for _ in range(28)]
students.sort()
all_students = [i+1 for i in range(30)]

for i in all_students:
	if i not in students:
		print(i)

# all_students = [i+1 for i in range(30)]

# for _ in range(28):
# 	student = int(input())
# 	all_students.remove(student)

# print(min(all_students))
# print(max(all_students))