# https://www.acmicpc.net/problem/15649
# N과 M (1)


def seq(idx):
    # idx가 M라면 arr 출력
    if idx == M:
        print(*arr)
        return
    for i in range(1, N+1):
        # 수열에 사용하지 않았다면 재귀
        if not used[i]:
            # 배열에 i값을 넣음
            arr[idx] = i
            used[i] = 1
            seq(idx+1)
            used[i] = 0


N, M = map(int, input().split())
arr = [0]*M
used = [0]*(N+1)
seq(0)