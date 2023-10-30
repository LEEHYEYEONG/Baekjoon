# n = int(input())
# n_list = []
# num = 2

# i = 1
# while(num < n):
#   num += i*6
#   n_list.append(num)
#   i+=1

# def solution(n):
#   if(n == 1):
#     return 1
#   elif(n < 7):
#     return 2
  
#   for i in range(n):
#     if(n_list[i] > n):
#       return i+2
#     elif(n_list[i] == n):
#       return i+3
  
# print(solution(n))

n = int(input())

nums, cnt = 1, 1
while n > nums:
    nums += 6 * cnt
    cnt += 1

print(cnt)