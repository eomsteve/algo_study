# 2841 / 외계인의 기타 연주
# https://www.acmicpc.net/problem/2841

N, P = map(int, input().split())
# [l, f]
melody = [list(map(int, input().split())) for _ in range(N)]

# 현재 누르고 있는 줄/플랫 을 마킹 해줄 배열
arr = [[] for _ in range(7)]
# 손가락 움직인 횟수
cnt = 0

for i, f in melody:
    # 아무것도 누르고있지 않는 경우
    if len(arr[i]) == 0:
        arr[i].append(f)
        cnt += 1

    else:
        # 현재 누르고있는 프렛보다 높은경우
        if f > arr[i][-1]:
            arr[i].append(f)
            cnt += 1
        # 현재 누르고있는 프렛과 같은경우
        elif f == arr[i][-1]:
            continue
        else:
            # 현재 누르고있는 프렛이 높은경우
            while len(arr[i]) != 0 and f < arr[i][-1]:
                arr[i].pop()
                cnt += 1
            # 높은 프렛을 뗀 후 같은 프렛이 있는경우
            if len(arr[i]) != 0 and arr[i][-1] == f:
                continue
            # 높은 프렛을 뗀 후 가장 높아진경우
            arr[i].append(f)
            cnt += 1

print(cnt)

### python3 / 시간 초과
### pypy3 / 통과