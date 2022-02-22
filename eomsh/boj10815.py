import sys
input = sys.stdin.readline


N = int(input())
n_num = list(map(int, input().split()))
M = int(input())
m_num = list(map(int, input().split()))
n_num.sort()


def bin_search(num, m_arr):
    start = 0
    end = len(m_arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if m_arr[mid] == num:
            return 1
        if num < m_arr[mid]:
            end = mid - 1
        if num > m_arr[mid]:
            start = mid + 1
    return 0


for i in m_num:
    print(f'{bin_search(i, n_num)}', end=' ')
