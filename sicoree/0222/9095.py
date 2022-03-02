# 9095 / 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095

T = int(input())
for tc in range(T):
    n = int(input())

    arr = [1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    if n > 2:
        for i in range(3, n + 1):
            arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
        
        print(arr[n])
    else:
        print(arr[n])

# n번째 항이 이전3개의 항을 합한것과 같음