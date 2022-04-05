def generate(arr, r, n, idx, chosen):
    global combi
    if len(chosen) == r:
        combi.append(chosen[:])
        return
    if idx == n:
        return
    chosen.append(arr[idx])
    generate(arr, r, n, idx+1, chosen)
    chosen.pop()
    generate(arr, r, n, idx + 1, chosen)

N = int(input())
power = [list(map(int, input().split())) for _ in range(N)]
combi = []
arr = range(1, N+1)
R = N//2
generate(arr, R, N, 1, [1])
new_combi = combi[:]
my_min = 38000
for i in range(len(new_combi)):
    start_sum = 0
    link_sum = 0
    combi = []
    generate(new_combi[i], 2, R, 0, [])
    for j in combi:
        start_sum += power[j[0]-1][j[1]-1]
        start_sum += power[j[1]-1][j[0]-1]
    combi = list(range(1, N+1))
    for j in new_combi[i]:
        combi.remove(j)
    new_combi[i] = combi[:]
    combi = []
    generate(new_combi[i], 2, R, 0, [])
    for j in combi:
        link_sum += power[j[0]-1][j[1]-1]
        link_sum += power[j[1]-1][j[0]-1]
    if abs(start_sum - link_sum) < my_min:
        my_min = abs(start_sum - link_sum)
print(my_min)