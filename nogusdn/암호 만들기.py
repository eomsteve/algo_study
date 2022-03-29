L, C = map(int, input().split())
arr = list(input().split())
ans = []
def selected(idx, password):
    if idx == C:
        if len(password) == L:
            cnt1 = 0
            cnt2 = 0
            for chr in password:
                if chr in 'aeiou':
                    cnt1 += 1
                else:
                    cnt2 += 1
            if cnt1 >= 1 and cnt2 >= 2:
                ans.append(password)
        return

    selected(idx+1, password+[arr[idx]])
    selected(idx+1, password)

selected(0, [])
for i in ans:
    i.sort()
ans.sort()
for i in ans:
    for j in i:
        print(j, end='')
    print()
