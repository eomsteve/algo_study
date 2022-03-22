N = int(input())
number = list(map(int, input().split()))
a, b, c, d = map(int, input().split())
max_v = -1000000000
min_v = 1000000000

def dfs(idx, ans, a, b, c, d):
    global max_v
    global min_v
    if idx == N:
        if ans > max_v:
            max_v = ans
        if ans < min_v:
            min_v = ans
        return
    if a:
        dfs(idx+1, ans+number[idx], a-1, b, c, d)
    if b:
        dfs(idx+1, ans-number[idx], a, b-1, c, d)
    if c:
        dfs(idx+1, ans*number[idx], a, b, c-1, d)
    if d:
        dfs(idx+1, int(ans/number[idx]), a, b, c, d-1)

dfs(1, number[0], a, b, c, d)
print(max_v)
print(min_v)

'''
처음에 출력 값이 다르길래 확인하니 나눗셈은 정수 값의 몫만 취한다고 하여서 int를 넣어주었다.
백트래킹 말고 permutation 사용해서도 풀 수 있을 거 같다. 
'''
