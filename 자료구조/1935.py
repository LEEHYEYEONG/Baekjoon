import sys

input = sys.stdin.readline
n = int(input())
array = list(input().strip())
num_dict = dict()

for i in range(n):
    num = int(input())
    num_dict[chr(65 + i)] = num

for i in range(len(array)):
    if array[i] in num_dict:
        array[i] = num_dict[array[i]]


def delete(array, value, i):
    array.insert(i + 1, value)
    del array[i - 2 : i + 1]
    return array


while len(array) != 1:
    for i in range(len(array)):
        if array[i] == "*":
            value = array[i - 2] * array[i - 1]
            array = delete(array, value, i)
            break
        elif array[i] == "/":
            value = array[i - 2] / array[i - 1]
            array = delete(array, value, i)
            break
        elif array[i] == "+":
            value = array[i - 2] + array[i - 1]
            array = delete(array, value, i)
            break
        elif array[i] == "-":
            value = array[i - 2] - array[i - 1]
            array = delete(array, value, i)
            break

print("{:.2f}".format(array[0]))

# 스택사용
n = int(input())
word = list(input())
num = [0] * n

for i in range(n):  # 피연산자 숫자 입력
    num[i] = int(input())

stack = []

for i in word:
    if "A" <= i <= "Z":
        stack.append(num[ord(i) - ord("A")])
    else:  # 연산자일시
        str2 = stack.pop()
        str1 = stack.pop()
        if i == "+":
            stack.append(str1 + str2)
        elif i == "-":
            stack.append(str1 - str2)
        elif i == "*":
            stack.append(str1 * str2)
        elif i == "/":
            stack.append(str1 / str2)
print("%.2f" % stack[0])
