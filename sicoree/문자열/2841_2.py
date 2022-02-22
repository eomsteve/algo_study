# 2841 / 외계인의 기타 연주
# https://www.acmicpc.net/problem/2841

N, P = map(int, input().split())
melody = [list(map(int, input().split())) for _ in range(N)]

# 현재 누르고 있는 줄/플랫 을 마킹 해줄 배열
arr = [[] for _ in range(7)]
# 손가락 움직인 횟수
cnt = 0

for i in range(N):
    # 해당 줄 내에서 누르고있는 가장 높은 프렛보다 높은경우
    if not arr[melody[i][0]] or arr[melody[i][0]][-1] < melody[i][1]:
        arr[melody[i][0]].append(melody[i][1])
        cnt += 1
        continue

    # 해당 줄 내에서 누르고있는 가장 낮은 프렛보다 낮을경우
    if melody[i][1] < arr[melody[i][0]][0]:
        cnt += len(arr[melody[i][0]]) + 1
        arr[melody[i][0]] = [melody[i][1]]
        continue

    # 누르고 있는 프렛중 프렛이 있거나, 그 사이에 프렛이 존재하는경우
    top = len(arr[melody[i][0]])
    for j in range(top - 1, -1, -1):
        if arr[melody[i][0]][j] <= melody[i][1]:
            top = j + 1
            break
    cnt += len(arr[melody[i][0]]) - top
    # 방금 누른 프렛 위에 프렛이 있을경우 떼줌
    if top != len(arr[melody[i][0]]):
        arr[melody[i][0]] = arr[melody[i][0]][:top]

    # 위 까지는 누르고 있는 프렛중 프렛이 있는 경우, 아래는 그 사이에 프렛이 존재하는 경우
    if arr[melody[i][0]][-1] != melody[i][1]:
        cnt += 1

print(cnt)

### python3 / 시간에러
### pypy3 / 틀림