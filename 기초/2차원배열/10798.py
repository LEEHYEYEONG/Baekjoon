a = [input() for i in range(5)]
max_len = max([len(a[i]) for i in range(5)])

for i in range(max_len):
  for j in range(5):
    try:
      print(a[j][i], end="")
    except:
      print(end="")

#words = [input() for i in range(5)]

# for j in range(15):
#     for i in range(5):
#         if j < len(words[i]):
#             print(words[i][j], end='')