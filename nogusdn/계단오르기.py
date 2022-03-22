N = int(input())
stair = []
for _ in range(N):
    stair.append(int(input()))
stair = stair[::-1]
max_v = 0
def dfs(idx, ans, check):
    global max_v
    if idx >= N-1 and check != 3:
        if ans > max_v:
            max_v = ans
        return
    if check != 3:
        dfs(idx+1, ans+stair[idx], check+1)
    dfs(idx+2, ans + stair[idx], 1)

dfs(1, stair[0], 1)
print(max_v)