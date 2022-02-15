arr = list(input().upper())
alphabet = ''
max_num = 0
same = 0
while len(arr) > 0:
    n = 1
    for i in range(1, len(arr)):
        if arr[0] == arr[i]:
            n += 1                  # arr[0]과 같은 것 개수 n에 저장
    a = arr[0]
    for i in range(n):
        arr.remove(a)           # arr[0]을 arr에서 n번 삭제
    if n > max_num:
        max_num = n             # n이 max_num보다 크면 max_num에 할당
        alphabet = arr[0]
    elif n == max_num:          # n이 max_num이랑 같으면 same에 할당
        same = n
if same == max_num:     # same == max_num이면 최댓값이 2개이므로 ? 출력
    print('?')
else:
    print(alphabet)         # 아니면 최댓값의 알파벳 출력

# 내장함수 안쓰려니까 시간 초과되네여ㅠㅠ