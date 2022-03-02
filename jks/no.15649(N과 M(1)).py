N, M = map(int, input().split())
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)
nums = []
result = []
for i in range(N):
    nums.append(i+1)
for i in range(M):
    result.append(nums.pop(0))
print(result)
for i in range(fact(N)//(fact(M)*fact(N-M))):