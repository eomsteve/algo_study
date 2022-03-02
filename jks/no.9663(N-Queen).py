N = int(input())
col_check = [0] * N
dia1_check = [0]*(N*2-1)
dia2_check = [0]*(N*2-1)
cnt = 0
def nqueen(idx):
    global cnt
    if idx == N:
        cnt += 1
        return
    for i in range(N):
        if not col_check[i] and not dia1_check[idx+i] and not dia2_check[idx-i+N-1]:
            col_check[i] += 1
            dia1_check[idx+i] += 1
            dia2_check[idx - i + N - 1] += 1
            nqueen(idx+1)
            col_check[i] -= 1
            dia1_check[idx + i] -= 1
            dia2_check[idx - i + N - 1] -= 1

nqueen(0)
print(cnt)