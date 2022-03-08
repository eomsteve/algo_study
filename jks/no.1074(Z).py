N, r, c = map(int, input().split())
N = 2**N
answer = 0
while N != 1:
    N //= 2
    if r < N:
        if c >= N:
            answer += N**2
            c %= N
    else:
        r %= N
        if c < N:answer += 2*N**2
        else:
            answer += 3*N**2
            c %= N

print(answer)
