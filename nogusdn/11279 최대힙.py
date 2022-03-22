import sys
last = 0
tree = [0]
def enq(n):
    global last
    last += 1
    tree.append(n) # tree[last] = n
    c = last
    p = c//2
    while p >= 1 and tree[p] < tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2

def deq():
    global last
    tmp = tree[1]
    tree[1] = tree[last]
    tree.pop()
    last -= 1
    p = 1
    c = p*2
    while c <= last:
        if c+1 <= last and tree[c] < tree[c+1]:
            c += 1
        if tree[c] > tree[p]:
            tree[c], tree[p] = tree[p], tree[c]
            p = c
            c = p*2
        else:
            break
    return tmp


N = int(input())
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(tree) == 1:
            print(0)
        else:
            print(deq())
    else:
        enq(num)


