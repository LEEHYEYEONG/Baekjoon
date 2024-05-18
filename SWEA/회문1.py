for i in range(10):
    n = int(input())

    count = 0

    # 원래 글자판
    mat = [list(map(str, input())) for _ in range(8)]

    # 반전된 글자판
    rev_mat = [[0 for _ in range(8)] for _ in range(8)]

    for j in range(8):
        for k in range(8):
            rev_mat[k][j] = mat[j][k]

    for j in range(8):
        for k in range(8):
            if k + n > 8:
                break
            word = "".join(mat[j][k : k + n])
            rev_word = "".join(rev_mat[j][k : k + n])

            new_word = "".join(reversed(word))
            new_rev_word = "".join(reversed(rev_word))

            if word == new_word:
                count += 1
            if rev_word == new_rev_word:
                count += 1

    print(f"#{i+1} {count}")
