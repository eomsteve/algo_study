N, M = map(int, input().split())
tree = list(map(int, input().split()))
start = 1
end = max(tree)
while start <= end:
    temp = 0
    mid = (start+end)//2
    for height in tree:
        if height > mid:
            temp += height-mid
    if temp >= M:
        start = mid + 1
        # result = mid
    else:
        end = mid - 1
# print(result)
print(end)




'''
어려웠던 점: 처음에는 tree 리스트를 만들어서 sort로 정렬하고 start값을 tree[0] end값을 tree[-1]로 하였는데
계속 런타임 에러가 나왔고 start값 을 1로 end값을 max(tree)로 수정하였는데도 계속 런타임에러가 뜸
그래서 result = mid로 하고 result를 출력했던 것을 print(end)로 바꾸니까 되었다.. (둘 다 값은 같음)
'''