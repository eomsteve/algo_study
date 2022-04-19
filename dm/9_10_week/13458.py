# https://www.acmicpc.net/problem/13458
# 시험 감독


N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = N
for i in range(len(A)):
    A[i] -= B
    if A[i] <= 0:
        continue
    cnt += A[i]//C +1 if A[i]%C else A[i]//C
print(cnt)
