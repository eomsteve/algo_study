# 2577번

# A, B, C = map(int, input().split())
#
# multi_v = A * B * C
#
# lst = [0] * 10
#
# for i in range(len(str(multi_v))):
#
#     n = multi_v % 10
#     lst[n] += 1
#     multi_v = multi_v // 10
#
# for i in lst:
#     print(i)

# 런타임 에러

'''
문제접근방식 : 입력 받은 배열 map을 사용하여 각각 받고 계산
반복문을 사용하여 각 자리수를 구한 뒤 해당하는 배열 순서에 값 증가

어려웠던점: 런타임 에러

설명이 필요한점?

'''

A = int(input())
B = int(input())
C = int(input())
multi_v_str = str(A*B*C)

for i in range(10):
    print(multi_v_str.count(str(i)))

'''
문제접근방식 : 맵핑을 사용하여 받으니 또다시 런타임 에러가 떠서 개별 값을 받은 후
런타임 에러를 피하기 위해 값을 str으로 받은 후 일단 count함수를 사용해보았다.

어려웠던점: count 안쓰고 하는 방법이 있을까요?

설명이 필요한점? 

'''