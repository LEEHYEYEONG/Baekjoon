# n = input()
# time = 0

# for i in range(len(n)):
#     a = ord(n[i])
#     if 65 <= a <= 67:
#         time += 3
#     elif a <= 70:
#         time += 4
#     elif a <= 73:
#         time += 5
#     elif a <= 76:
#         time += 6
#     elif a <= 79:
#         time += 7
#     elif a <= 83:
#         time += 8
#     elif a <= 86:
#         time += 9
#     else:
#         time += 10

# print(time)

dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

text = input()
time = 0

for i in text:
    for j in dial:
        if i in j:
            time += dial.index(j) + 3

print(time)
