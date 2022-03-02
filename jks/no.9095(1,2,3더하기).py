T = int(input())
for tc in range(T):
    def fact(n):
        if n <= 1:
            return 1
        else:
            return n * fact(n - 1)
    N = int(input())
    n_sum = 0
    for a in range(N//3 + 1):
        for b in range((N - a*3)//2 + 1):
            c = N - a*3 - b*2
            n_sum += fact(a+b+c)//(fact(a)*fact(b)*fact(c))
    print(n_sum)