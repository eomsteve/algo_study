N = int(input())
cost = list(map(int, input().split()))
M = int(input())
start = 0
end = max(cost)
def binarysearch(start, end):
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for c in cost:
            if c <= mid:
                cnt += c
            else: # 상한액 보다 크면
                cnt += mid
        if cnt > M:
            end = mid - 1
        else:
            start = mid + 1

    return end

print(binarysearch(start,end))