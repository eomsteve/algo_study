N, M = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()
distance = house[-1] - house[0]
start = 1
result = 0
while start <= distance:
    mid = (start+distance) // 2
    cnt = 1
    cur = house[0]
    for i in range(1, N):
        if house[i] - cur >= mid:
            cnt += 1
            cur = house[i]

    if cnt >= M:
        start = mid+1
        result = mid
    else:
        distance = mid-1

print(result)

# readline으로 입력받으면 pypy3로 안해도 풀린다.