for i in range(10):
    n = int(input())

    palindrome = 0

    # 원래 글자판
    mat = [list(input()) for _ in range(100)]

    # 반전된 글자판
    rev_mat = [x for x in zip(*mat)]

    # 가장 큰 개수인 100개 부터 ~1개 까지 검사
    def check(mat, rev_mat):
        for j in range(100, 0, -1):
            for k in range(100 - j + 1):
                for l in range(100 - j + 1):
                    if l+j > 100:
                        break

                    word = mat[k][l:l+j]
                    rev_word = rev_mat[k][l:l+j]

                    if word == word[::-1] or rev_word == rev_word[::-1]:
                        return j

    print(f"#{n} {check(mat,rev_mat)}")