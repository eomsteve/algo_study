############
# 정렬 정리 #
############
# 참고 사이트
# https://www.daleseo.com/?tag=algorithm
# https://gyoogle.dev/blog/

import time
import datetime
import random
# 뒤에서 부터 앞으로 정렬하는 구조
# 가장 큰 값을 맨 뒤로 보내고, 그 다음 큰값을 바로 앞에 보내는 형태
# swap이 빈번하게 일어남
# 루프문을 통해 뒤부터 모든 인덱스 접근 * 인접한 값들의 대소비교 및 자리교대 = O(N)*O(N) = O(N^2)
def bubble_sort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
# 이전 pass에서 교환이 한번도 일어나지 않았자면, 정렬할 값이 없다고 간주
def bubble_sort2(a):
    for i in range(len(a)-1, 0, -1):
        swap = False
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swap = True
        if not swap:
            break
# swap체크 대신, 마지막으로 교환이 있었던 인덱스를 저장해 그 전까지만 정렬
def bubble_sort3(a):
    end = len(a)-1
    while end > 0:
        l_swap = 0
        for i in range(end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                l_swap = i
        end = l_swap
# 가장 작은값을 찾아 맨 앞으로 가져옴
# 모든 인덱스 접근 * 최솟값을 찾은 후 현재 인덱스와 교환 = O(N)*O(N) = O(N^2)
def selection_sort(a):
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[min_idx] > a[j]:
                min_idx = j
        a[min_idx], a[i] = a[i], a[min_idx]
# 앞의 원소들과 비교해 삽입할 위치를 지정 후, 원소를 뒤로 옮기고 자리에 삽입
# 범위2부터 전체로 범위 확장 * 추가된 값과 기존 값들의 대소 비교 및 자리 교환 = O(N)*O(N) = O(N^2)
def insertion_sort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
# 정렬할 값보다 작은 숫자를 만나는 최초의 순간 반복문 정지
def insertion_sort2(a):
    for end in range(1, len(a)):
        i = end
        while i > 0 and a[i-1] > a[i]:
            a[i-1], a[i] = a[i], a[i-1]
            i -= 1
# swap 없이 단순히 값들을 shift 시키기
def insertion_sort3(a):
    for end in range(1, len(a)):
        to_insert = a[end]
        i = end
        while i > 0 and a[i-1] > to_insert:
            a[i] = a[i-1]
            i -= 1
        a[i] = to_insert
# 분할 정복 기법과 재귀 알고리즘을 이용해 정렬하는 알고리즘, 배열을 크기가 1이 될 때까지 둘로 쪼갠 후 크기순으로 재배열 하면서 원래 크기의 배열로 합침
# 반복의 수가 절반으로 점점 줄어듦 * 각 패스에서 병합할 때 모든 값을 비교 = O(logN) * O(N) = O(NlogN)
def merge_sort(a):
    if len(a) < 2:
        return a
    
    mid = len(a) // 2
    low_arr = merge_sort(a[:mid])
    high_arr = merge_sort(a[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr
# slice를 사용할 때 배열의 복제가 일어나므로 idx로 직접 접근함
def merge_sort2(a):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)
    
    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if a[l] < a[h]:
                temp.append(a[l])
                l += 1
            else:
                temp.append(a[h])
                h += 1
            
        while l < mid:
            temp.append(a[l])
            l += 1
        while h < high:
            temp.append(a[h])
            h += 1

        for i in range(low, high):
            a[i] = temp[i - low]
    
    return sort(0, len(a))
# 분할 정복 기법과 재귀 알고리즘을 이용, 피봇이라 불리는 임의의 기준값을 사용
# 기본적으로 O(NlogN)이지만, 값이 치우쳐있으면 최악의경우 O(N^2)를 가짐
def quick_sort(a):
    if len(a) < 2:
        return a
    pivot = a[len(a) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in a:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
# 재귀를 사용할 때 마다 새로운 배열이 생성되므로
def quick_sort2(a):
    def sort2(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort2(low, mid-1)
        sort2(mid, high)

    def partition(low, high):
        pivot = a[(low + high) // 2]
        while low <= high:
            while a[low] < pivot:
                low += 1
            while a[high] > pivot:
                high -= 1
            if low <= high:
                a[low], a[high] = a[high], a[low]
                low, high = low+1, high-1
        return low
    
    return sort2(0, len(a)-1)
# 사용하는 숫자만큼의 count_arr를 만들고 이것을 이용해 정렬함
def counting_sort(a, max):
    count_arr = [0]*(max+1)
    for i in a:
        count_arr[i] += 1
    
    for i in range(max):
        count_arr[i+1] += count_arr[i]
    
    output_arr = [-1]*len(a)
    for i in a:
        output_arr[count_arr[i]-1] = i
        count_arr[i] -= 1
    return output_arr


# 추가예정 #
# 힙 정렬(Heap Sort)
# 셸 정렬(shell Sort)
# 기수 정렬(Radix Sort)


count_num = 1000000
arr = [random.randint(0,count_num) for _ in range(5000)]
arr0, arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9 = arr[:], arr[:], arr[:], arr[:], arr[:], arr[:], arr[:], arr[:], arr[:], arr[:]
arr10, arr11, arr12, arr13, arr14, arr15, arr16, arr17, arr18, arr19 = arr[:], arr[:], arr[:], arr[:], arr[:], arr[:], arr[:], arr[:], arr[:], arr[:]


start = time.time()
arr0 = sorted(arr0)
end = time.time()
print('sorted:', datetime.timedelta(seconds= end-start), arr0[:5])

start = time.time()
bubble_sort(arr1)
end = time.time()
print('bubble_sort:', datetime.timedelta(seconds= end-start), arr1[:5])

start = time.time()
bubble_sort2(arr2)
end = time.time()
print('bubble_sort2:', datetime.timedelta(seconds= end-start), arr2[:5])

start = time.time()
bubble_sort3(arr3)
end = time.time()
print('bubble_sort3:', datetime.timedelta(seconds= end-start), arr3[:5])

start = time.time()
selection_sort(arr4)
end = time.time()
print('selection_sort:', datetime.timedelta(seconds= end-start), arr4[:5])

start = time.time()
insertion_sort(arr5)
end = time.time()
print('insertion_sort:', datetime.timedelta(seconds= end-start), arr5[:5])

start = time.time()
insertion_sort2(arr6)
end = time.time()
print('insertion_sort2:', datetime.timedelta(seconds= end-start), arr6[:5])

start = time.time()
insertion_sort3(arr7)
end = time.time()
print('insertion_sort3:', datetime.timedelta(seconds= end-start), arr7[:5])

start = time.time()
arr8 = merge_sort(arr8)
end = time.time()
print('merge_sort:', datetime.timedelta(seconds= end-start), arr8[:5])

start = time.time()
merge_sort2(arr9)
end = time.time()
print('merge_sort2:', datetime.timedelta(seconds= end-start), arr9[:5])

start = time.time()
arr10 = quick_sort(arr10)
end = time.time()
print('quick_sort:', datetime.timedelta(seconds= end-start), arr10[:5])

start = time.time()
quick_sort2(arr11)
end = time.time()
print('quick_sort2:', datetime.timedelta(seconds= end-start), arr11[:5])

start = time.time()
arr12 = counting_sort(arr12, count_num)
end = time.time()
print('counting_sort:', datetime.timedelta(seconds= end-start), arr12[:5])
