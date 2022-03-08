# 2512 / 예산
# https://www.acmicpc.net/problem/2512

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

arr.sort()

sum_arr = 0
for i in arr:
    sum_arr += i

if sum_arr <= M:
    print(arr[-1])
else:
    for i in range(N):
        if arr[i] * (N - i) > M:
            print(M // (N - i))
            break
        else:
            M -= arr[i]

### 접근방법
# 오름차순으로 정렬하여 아래부터 조건에 맞지않으면 빼주는 방식으로 구현