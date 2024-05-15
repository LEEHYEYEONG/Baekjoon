for i in range(10):
    n = int(input())

    # 2차원 입력받기
    mat = [list(map(int, input().split())) for _ in range(100)]

    max_row = max([sum(mat[j]) for j in range(100)])

    # 전치행렬
    new_mat = [[0 for _ in range(100)] for _ in range(100)]

    for j in range(100):
        for k in range(100):
            new_mat[k][j] = mat[j][k]

    max_col = max([sum(new_mat[j]) for j in range(100)])

    dias = sum([mat[j][j] for j in range(100)])
    rev_dias = sum([mat[j][99 - j] for j in range(100)])

    print(f"#{i+1} {max([max_row, max_col, dias, rev_dias])}")
