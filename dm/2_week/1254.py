# https://www.acmicpc.net/problem/1254
# 팰린드롬 만들기


def p_string(str_a):
    # 겹치는 값이 없을경우
    min_len = (len(str_a)-1)*2 + 1
    for i in range(len(str_a)-1):
        # 팰린드롬이 짝수인 경우
        # str_a[i] == str_a[i+1]를 찾았을 때 일부가 같고, 틀렸을 경우를 판단하기 위해 p_flag를 넣음
        p_flag = 0
        if str_a[i] == str_a[i+1]:
            d = 0
            while i+1 + d < len(str_a):
                if i - d < 0:
                    p_flag = 0
                    break
                # +,-를 비교해가며 팰린드롬이 될만한지 판단함
                if str_a[i-d] == str_a[i+1+d]:
                    d += 1
                    p_flag = 1
                else:   # 팰린드롬이 아닌경우
                    p_flag = 0
                    break
            # 가장 짧은 단어의 갯수를 min_len 에 넣음
            if p_flag == 1 and min_len > len(str_a) + (i-d+1):
                min_len = len(str_a) + (i-d+1)           
        # 팰린드롬이 홀수인 경우 짝수와 비슷하게 반복
        p_flag = 0
        if str_a[i-1] == str_a[i+1]:
            d = 0
            while i + d < len(str_a):
                if i - d < 0:
                    p_flag = 0
                    break
                if str_a[i-d] == str_a[i+d]:
                    d += 1
                    p_flag = 1
                else:   # 팰린드롬이 아닌경우
                    p_flag = 0
                    break
            if p_flag == 1 and min_len > len(str_a) + (i-d+1):
                min_len = len(str_a) + (i-d+1)
    return min_len
# 팰린드롬의 조건
# 1. 문자열이 짝수인경우, i = max_idx, i//2, i//2 + 1 과, +,-가 같음
# 2. 문자열이 홀수인경우, i//2 를 기준으로 +,- 가 같음
p_str = input()
print(p_string(p_str))



'''
문제 접근 방식
- 문자열중 팰린드롬의 형태를 띈 문자열이 발견되지 않았을경우, 짝수인경우, 홀수인경우로 나눠서 생각함.

어려웠던 점
- 처음 d = 1 이라고 가정을 했는데 abaa 이렇게 짝수인데 d=0으로 끝나는 경우가 있었어서 틀림..

설명이 필요한점

'''