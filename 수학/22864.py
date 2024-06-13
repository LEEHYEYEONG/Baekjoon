a, b, c, m = map(int, input().split())

# 24시간이 되는지 체크하는 변수
hours = 0

# 현재 피로도
hard = 0

# 처리한 일
work = 0

while hours != 24:
    # 피로도가 한시간 더 일하면 m을 넘으면 한시간 쉬기
    if hard + a > m:
        # 피로도 음수가 되지 않게 체크
        hard = hard - c if hard - c >= 0 else 0
    else:
        work += b
        hard += a
    hours += 1

print(work)
