# 1254 / 팰린드롬 만들기
# https://www.acmicpc.net/problem/1254

arr = list(input())
idx = 0

while idx < len(arr):
    l_arr = int(len(arr) / 2)
    for i in range(l_arr):
        if arr[i] != arr[-i - 1]:
            for j in range(idx):
                arr.pop()
            for j in range(idx, -1, -1):
                arr.append(arr[j])
            idx += 1
            break
    else:
        idx = len(arr)

print(len(arr))

### 접근방법
# 문자열이 회문인지 확인한 후, 회문이아니라면 n번째 글자 까지
# 문자열 뒤에 역으로 추가하여 회문이 될때까지 반복하는 반복문 구현