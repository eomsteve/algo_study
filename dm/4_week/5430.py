# https://www.acmicpc.net/problem/5430
# AC


T = int(input())
for _ in range(T):
    rd = input()
    N = int(input())
    # 괄호를 떼고 입력을 받음
    arr = input().lstrip('[').rstrip(']')
    # 문자열이 비어있지 않으면, ','으로 구분해 리스트에 담음
    if arr:
        arr = arr.split(',')
    idx = 0
    result = ''
    for c in rd:
        # R이라는 문자열을 받으면
        if c == 'R':
            # 뒤에서부터 찾음
            idx = idx*(-1)-1
        # D라는 문자열을 받으면
        else:
            if arr:
                # 현재 idx에 있는 값을 pop함
                arr.pop(idx)
            else:
                result = 'error'
                break
    # idx가 -1이라면, 뒤집혀있다고 생각하고 배열을 뒤집음
    if idx:
        arr = arr[::-1]
    # 결과값 출력
    if not result:
        result = ','.join(arr)
        print(f'[{result}]')
    else:
        print(result)
