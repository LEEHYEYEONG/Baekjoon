n = int(input())
area = 0

white_paper = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
  w, h = map(int, input().split())
  for i in range(10):
    for j in range(10):
      if(white_paper[w+i][h+j] == 0):
        white_paper[w+i][h+j] = 1

for i in range(100):
  area += white_paper[i].count(1)

print(area)


