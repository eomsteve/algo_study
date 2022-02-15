# O O O 이 등차수열이면 한수
N = int(input())
cnt = 0

if N > 99: # N이 3자리 수  abc  b - a == c - b
    for num in range(100, N+1):
        a = num//100  # 100의자리
        b = (num%100)//10 #10의자리
        c = num % 10  #1의자리
        if b-a == c-b:
            cnt += 1
    print(cnt + 99)
else:
    print(N)