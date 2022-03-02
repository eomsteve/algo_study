T = int(input())
for tc in range(1, T+1):
    N = int(input())

    def solve(N):
        if N == 1:
            return 1
        elif N == 2:
            return 2
        elif N == 3:
            return 4
        return solve(N-1) + solve(N-2) + solve(N-3)
    print(solve(N))