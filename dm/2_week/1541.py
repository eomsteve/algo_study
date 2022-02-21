# https://www.acmicpc.net/problem/1541
# 잃어버린 괄호


# 숫자, +, - 3종류의 데이터만 들어가 있음, 최솟값 찾기
# -를 기준으로 숫자를 나눠줌
# 그것을 +로 나눠 더해줌
# -를 기준으로 나눈 값을 연산함
minus_arr = list(input().split('-'))
for i in range(len(minus_arr)):
    minus_arr[i] = sum(list(map(int, minus_arr[i].split('+'))))
# 인덱싱은 인덱스값이 없으면 에러가 나지만, 슬라이싱은 없으면 빈 배열을 return 받음
print(minus_arr[0] - sum(minus_arr[1:]))



'''
문제 접근 방식
- -로 split 해 첫 idx 에 나머지를 모두 빼주면 최솟값

어려웠던 점
- 

설명이 필요한점
# 인덱스의 경우 1, 슬라이싱의경우 [1]을 반환함
# arr = [1, 2, 3]
# print(arr[0], arr[0:1])
'''