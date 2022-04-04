# https://www.acmicpc.net/problem/1759
# 암호 만들기


def sol(idx, vow, con, eng):
    if idx == L:
        if vow >= 1 and con >= 2:
            print(eng)
        return
    for a in range(C):
        if not v[a]:
            if idx > 0 and alpa[eng[-1]] > alpa[arr[a]]:
                continue
            v[a] = 1
            if arr[a] in vowel:
                sol(idx+1, vow+1, con, eng+arr[a])
            else:
                sol(idx+1, vow, con+1, eng+arr[a])
            v[a] = 0


alpa = {chr(x+ord('a')):x for x in range(26)}
vowel = ['a', 'e', 'i', 'o', 'u']
L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
v = [0]*C
sol(0, 0, 0, '')
