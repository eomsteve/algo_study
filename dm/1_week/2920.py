# https://www.acmicpc.net/problem/2920
# 음계


scale = list(map(int, input().split()))
sum_val = 0
for i in range(len(scale)-1):
    compare_scale = scale[i+1] - scale[i]
    if compare_scale == 1:
        sum_val += 1
    elif compare_scale == -1:
        sum_val -= 1
    else:
        break

if sum_val == 7:
    print('ascending')
elif sum_val == -7:
    print('descending')
else:
    print('mixed')



'''
문제 접근 방식
- 입력을 list로 받아 순서대로 비교하면서, 값 차이가 1또는 -1이면 값을 더하고, 그 외의값은
반복문을 탈출함. 마지막으로 더한 값이 7이나 -7이면 연속된 수라고 판단해 ascending, descending을
출력하고 나머지는 mixed을 출력함

어려웠던 점

설명이 필요한점

'''