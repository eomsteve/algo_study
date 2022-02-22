N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
new_B = [0] * M
for i in range(M):
    for j in range(N):
        if A[i] == B[j]:
            B[j] = 1
            break
    else:
        B[j] = 0
print(*B)


'''
문제접근방식 : B의 숫자가 A에 있는지 확인 후 있으면 1, 없으면 0으로 바꿈

어려웠던점: 시간 초과ㅠㅠ

설명이 필요한점?
'''