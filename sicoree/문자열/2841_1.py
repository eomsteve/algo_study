# 2841 / 외계인의 기타 연주
# https://www.acmicpc.net/problem/2841

N, P = map(int, input().split())
melody = [list(map(int, input().split())) for _ in range(N)]

# 현재 누르고 있는 줄/플랫 을 마킹 해줄 배열
arr = [[0] * (P + 1) for _ in range(7)]
# 손가락 움직인 횟수
cnt = 0
for i in range(N):
    # 현재 안누르고 있는 자리라면 눌러주고 손가락횟수 + 1
    if arr[melody[i][0]][melody[i][1]] == 0:
        arr[melody[i][0]][melody[i][1]] = 1
        cnt += 1
        # 방금 누른 곳 위쪽 프렛을 누르고있었다면 다 떼주고 떼준만큼 + n
        for j in range(melody[i][1] + 1, 16):
            if arr[melody[i][0]][j] == 1:
                arr[melody[i][0]][j] = 0
                cnt += 1
    else:
        # 방금 튕긴 프렛의 위쪽 프렛을 누루고 있었다면 다 떼주고 떼준만큼 + n
        for j in range(melody[i][1] + 1, 16):
            if arr[melody[i][0]][j] == 1:
                arr[melody[i][0]][j] = 0
                cnt += 1
print(cnt)

### python3 / 시간초괴
### pypy3 / 틀림
# 스택 형식으로 다시 해봐야 할것같음