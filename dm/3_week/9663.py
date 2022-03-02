# https://www.acmicpc.net/problem/9663
# N-Queen


def n_queen(idx):
    # idx가 N이 되면 각 행에 퀸이 모두 놓였다 판단한다.
    global cnt
    if idx == N:
        cnt += 1
        return
    # 퀸을 하나 놓으면, 그 열은 모두 놓을 수 없다.
    # 퀸을 하나 놓으면, 그 대각선은 모두 놓을 수 없다.
    # idx 이전행의 대각선을 현재 idx에 맞게 변환시켜 제한사항을 둠
    notloc = []
    for i in range(idx):
        # loc의 index와 i를 연산해 현재 idx의 위치일 때 있어서 안될 위치를 표시
        # loc[i] 에서 index와 idx의 차이만큼 위치해서 안된다.
        notloc.append(loc[i]-(idx-i))
        notloc.append(loc[i]+idx-i)
        # 단 이것은 0 <= a < N 이다.
    # 다음 idx를 판단한다.
    for i in range(N):
        if loc[idx] == -1 and not ((i in loc) or (i in notloc)):
            loc[idx] = i
            n_queen(idx+1)
            loc[idx] = -1


N = int(input())
loc = [-1]*N
cnt = 0
n_queen(0)
print(cnt)
