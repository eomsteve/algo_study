N, K = map(int, input().split())
lan = [int(input()) for _ in range(N)]
start = 0
end = (sum(lan)//K)*2
while True:
    n = 0
    mid = (start + end)//2
    for i in range(N):
        n += lan[i]//mid
    if n == K:
        while True:
            mid += 1
            n = 0
            for j in range(N):
                n += lan[j] // mid
            if n != K:
                print(mid-1)
                break
        break
    elif n > K:
        start = mid
    else:
        end = mid

'''
문제접근방식 : 단순히 랜선 길이를 다 더하고 필요한 갯수로 나누었을 때의 값을 avr로 두고 랜선들에서 avr로 나눈 몫의 합이 11이 될 때까지 이진탐색.
탐색하고 나면 1씩 더하면서 최댓값 찾기

어려웠던점: 시간.................

설명이 필요한점?
'''