N = int(input())
col_check = [0] * N
dia1_check = [0] * (N*2-1)
dia2_check = [0] * (N*2-1)
cnt = 0


def n_queen(idx):
    global cnt
    if idx == N:
        cnt += 1
        return
    for i in range(N):
        if not col_check[i] and not dia1_check[idx + i] and not dia2_check[idx - i + N - 1]:
            col_check[i] += 1
            dia1_check[idx + i] += 1
            dia2_check[idx - i + N - 1] += 1
            n_queen(idx + 1)
            col_check[i] -= 1
            dia1_check[idx + i] -= 1
            dia2_check[idx - i + N - 1] -= 1


n_queen(0)
print(cnt)

# answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
# print(answer[int(input())])