arr = list(input().upper())
nums = []
for i in range(len(arr)):
    nums.append(arr.count(arr[i]))
if nums.count(max(nums)) > max(nums):
    print('?')
else:
    for i in range(len(nums)):
        if nums[i] == max(nums):
            print(arr[i])
            break

# 내장함수 써도 시간초과 나네요ㅠㅠㅠㅠㅠㅠㅠ 어떻게 더 줄이죠..??