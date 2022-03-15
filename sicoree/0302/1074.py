# 1074 / Z
# https://www.acmicpc.net/problem/1074
def Z(n, r, c):
    if n == 1:
        if r == 0:
            if c == 0:
                return 0
            else:
                return 1
        else:
            if c == 0:
                return 2
            else:
                return 3

    else:
        # 1사분면
        if r < 2 ** (n - 1) and c < 2 ** (n - 1):
            return Z(n - 1, r, c)

        # 2사분면
        elif r < 2 ** (n - 1) and c >= 2 ** (n - 1):
            c -= 2 ** (n - 1)
            return 2 ** ((n - 1) * 2) + Z(n - 1, r, c)

        # 3사분면
        elif r >= 2 ** (n - 1) and c < 2 ** (n - 1):
            r -= 2 ** (n - 1)
            return (2 ** ((n - 1) * 2)) * 2 + Z(n - 1, r, c)

        # 4사분면
        elif r >= 2 ** (n - 1) and c >= 2 ** (n - 1):
            r -= 2 ** (n - 1)
            c -= 2 ** (n - 1)
            return (2 ** ((n - 1) * 2)) * 3 + Z(n - 1, r, c)


N, r, c = map(int, input().split())

result = Z(N, r, c)

print(result)

### 접근방법
# 가장 큰 정사각형부터 4분면씩 계속 쪼개들어가며 값을 넘겨준다
# 그렇게 가장 작은 2 * 2 정사각형이 되었을때 최종값을 리턴
### 어려웠던점
# 처음에 배열로 접근했는데 메모리 초과가 발생하여
# 배열을 없애고 값을 넘겨주는 방법을 활용하였다