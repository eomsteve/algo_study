tall = []
tall_sum = 0
for i in range(9):
    t = int(input())
    tall.append(t)
    tall_sum += t
is_find = 0
for i in range(9):
    for j in range(9):
        if i != j:
            if tall[i] + tall[j] == tall_sum - 100:
                a = tall[i]
                b = tall[j]
                tall.remove(a)
                tall.remove(b)
                is_find = 1
                break
    if is_find == 1:
        break
for i in range(7):
    for j in range(i+1, 7):
        if tall[i] > tall[j]:
            tall[i], tall[j] = tall[j], tall[i]
for i in range(7):
    print(tall[i])