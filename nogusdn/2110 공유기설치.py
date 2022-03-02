N, C = map(int, input().split()) # 집 개수, 공유기 개수
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort() # 1 2 4 8 9
start = 1
end = arr[-1] - arr[0] # 두 거리간의 가장 큰 gap 부터 조사하기 위해서

while start <= end: # 이진검색
    mid = (start+end)//2 # mid 값이 즉 공유기 설치 간격
    current = arr[0] # 현재 위치는 arr[0]
    cnt = 1 # arr[0]에 공유기를 설치하므로

    for i in range(1, len(arr)):
        if arr[i] >= current+mid: # 현재 값에 공유기 설치간격을 더 한 것 보다 큰 장소가 있으면 설치
            cnt += 1
            current = arr[i]
    if cnt >= C: # 만약에 카운트가 공유기 개수 이상이 된다면 result에 mid값 저장하고 간격 더 큰 것 있는 지 확인
        start = mid + 1
    else: # 만약에 카운트가 공유기 개수보다 작다면 설치 간격을 줄여야 하므로
        end = mid - 1

print(end)


'''
어려웠던 점: 이진탐색으로 최적의 간격을 구하는 것 + 문제 이해하기가 처음 접근하기가 어려웠다.

'''
