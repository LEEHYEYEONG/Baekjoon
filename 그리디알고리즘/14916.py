n = int(input())

answer = []

five = 0

while True:
    tmp = (n - five * 5) % 2
    if tmp == 0:
        answer.append((n - five * 5) // 2 + five)
    five += 1
    if five * 5 > n:
        break

if answer:
    print(min(answer))
else:
    print(-1)
