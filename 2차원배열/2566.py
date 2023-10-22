arr = [list(map(int, input().split())) for _ in range(9)]

max_arr = max(arr[0])
max_index = 0

for i in range(9):
  if(max_arr <= max(arr[i])):
    max_arr = max(arr[i])
    max_index = i
  
print(max_arr)
print(max_index+1, arr[max_index].index(max_arr)+1)