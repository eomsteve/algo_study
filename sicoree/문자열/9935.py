# 9935 / 문자열 폭발
# https://www.acmicpc.net/problem/9935

arr = list(input())
boom = list(input())

result = []
for i in arr:
    if len(result) == 0:
        result.append(i)
    else:
        for j in range(len(boom) - 1, -1, -1):
            if boom[j] != i:
                result.append(i)
                break
        else:
            for j in range(len(boom) - 1):
                result.pop()
print(result)