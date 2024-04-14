from collections import defaultdict

n = int(input())

seat = [[0 for _ in range(n)] for _ in range(n)]

fav = defaultdict(list)

for _ in range(n**2):
    student = list(map(int, input().split()))
    fav[student[0]] = student[1:]

    for i in range(n):
        for j in range(n):
            fav_count = 0
            # 비어있지 않으면 넘어감
            if seat[i][j] == 0:
                continue
            # 비어있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 칸 확인
            for _ in range(4):
                if j - 1 >= 0 and seat[i][j] in fav[student[0]]:
                    fav_cou
# print(fav)
