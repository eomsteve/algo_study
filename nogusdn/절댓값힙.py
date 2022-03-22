import sys
tree = [0]
last = 0
def enq(v):
    global last
    last += 1
    tree.append(v)
    c = last
    p = c//2
    while p >= 1:
        if abs(tree[p]) > abs(tree[c]):
            tree[p], tree[c] = tree[c], tree[p]

        if abs(tree[p]) == abs(tree[c]) and tree[p] > tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2


def deq():
    global last
    tmp = tree[1]
    tree[1] = tree[last]
    tree.pop()
    last -= 1
    p = 1
    c = p*2
    while c <= last:
        if c + 1 <= last and abs(tree[c]) > abs(tree[c+1]): # 오른쪽 값이 있으면서 오른쪽 값이 왼쪽보다 작으면 오른쪽 값 선택
            c += 1
        elif c + 1 <= last and abs(tree[c]) == abs(tree[c+1]):
            if tree[c+1] < tree[c]:
                c += 1
        if abs(tree[c]) < abs(tree[p]):
            tree[c], tree[p] = tree[p], tree[c]
            p = c
            c = p*2
        else:
            break
    return tmp

N = int(input())
for _ in range(N):
    v = int(sys.stdin.readline())
    if v == 0:
        if len(tree) == 1:
            print(0)
        else:
            print(deq())
    else:
        enq(v)