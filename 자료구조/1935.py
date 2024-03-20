from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
array = deque(list(input().strip()))
num = deque([int(input()) for _ in range(n)])


def delete(array, value, i):
    array.insert(i + 1, value)
    del array[i]
    del array[i - 1]
    del array[i - 2]
    return array


for i in range(len(array)):
    if array[i].isalpha():
        array[i] = num.popleft()
    else:
        continue

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
