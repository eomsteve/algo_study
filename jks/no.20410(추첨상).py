m, Seed, X1, X2 = map(int, input().split())
is_find = 0
for a in range(99):
    for c in range(99):
        if X1 == (a * Seed + c) % m:
            if X2 == (a * X1 + c) % m:
                is_find = 1
                print(a, c)
                break
    if is_find == 1:
        break
