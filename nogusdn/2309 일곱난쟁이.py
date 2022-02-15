height_list = [int(input()) for _ in range(9)]
for i in range(9):
    for j in range(i+1, 9):
        if sum(height_list) - height_list[i] - height_list[j] == 100:
            a,b = height_list[i], height_list[j]
            height_list.remove(a)
            height_list.remove(b)
            for height in sorted(height_list):
                print(height)
            break
    if len(height_list) == 7:
        break
        
