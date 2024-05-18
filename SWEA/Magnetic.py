for i in range(10):
    n = int(input())

    count = 0

    table = [list(map(str, input().split())) for _ in range(n)]
    rev_table = [[0 for _ in range(n)] for _ in range(n)]

    # 가로로 변경
    for j in range(n):
        for k in range(n):
            rev_table[k][j] = table[j][k]

    for j in rev_table:
        # 0 제거
        string = list(("".join(j)).replace("0", ""))
        # 앞에 자석 체크
        n_mag, s_mag = False, False
        # 처음 체크 변수
        first, end = True, False
        for k in range(len(string)):
            # s극인 경우
            if string[k] == "2":
                s_mag = True
                # n극이 아직 나오지 않은 경우 -> 테이블 밑으로 떨어짐
                if first:
                    continue
                # n극 나온 후 s극 -> 교착상태
                if n_mag:
                    count += 1
                    n_mag = False
            # n극인 경우
            elif string[k] == "1":
                n_mag = True
                # 처음 나오는 n극인 경우
                if first:
                    first = False
                # n극 뒤에 s가 없는 경우 -> 종료
                if "2" not in string[k + 1 : 100]:
                    break

    print(f"#{i+1} {count}")
