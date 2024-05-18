T = int(input())

# 딕셔너리
num_dict = {
    "ZRO": 0,
    "ONE": 1,
    "TWO": 2,
    "THR": 3,
    "FOR": 4,
    "FIV": 5,
    "SIX": 6,
    "SVN": 7,
    "EGT": 8,
    "NIN": 9,
}

# 딕셔너리 key, value 뒤집어서
rev_num_dict = {}
for k, v in num_dict.items():
    rev_num_dict[v] = k

for i in range(T):
    test, N = map(str, input().split())
    N = int(N)

    word_list = list(input().split())
    num_list = []

    # 단어 -> 숫자로 변환
    for j in range(N):
        num_list.append(num_dict[word_list[j]])

    # 정렬 후 숫자 -> 단어로 변환
    num_list.sort()

    for j in range(N):
        num_list[j] = rev_num_dict[num_list[j]]

    print(test)
    print(*num_list)
