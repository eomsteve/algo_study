# 55+20-50+40-30+20

data = input().split('-') # [55+20, 50+40, 30+20] 첫번째 값은 제외해야하구나
cnt = 0
temp = []
for i in range(1, len(data)): # 첫번째 값 이후부터 '+' split하고 cnt에 - 해준다.
    temp = data[i].split('+')
    for num in temp:
        cnt -= int(num)
if '+' in data[0]: # 만약에 첫번째 값에 +가 있다면 분리해서 int로 더 해줘야함
    print(sum(map(int, data[0].split('+'))) + cnt)
else: # 없으면 그냥 더해주면 됨
    print(int(data[0]) + cnt)
