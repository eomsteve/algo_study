
def solve(n, alst, blst):
    global ans
    if n == N:
        if len(alst) == len(blst):
            asum = 0
            bsum = 0
            for i in range(len(alst)):
                for j in range(len(alst)):
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            if ans > abs(asum-bsum):
                ans = abs(asum-bsum)
        return

    solve(n+1, alst+[n], blst)
    solve(n+1, alst, blst+[n])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 99999
solve(0, [], [])
print(ans)