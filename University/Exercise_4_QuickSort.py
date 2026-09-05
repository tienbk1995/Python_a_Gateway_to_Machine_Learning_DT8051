# SOLUTION TO EXERCISE 4
import time, random

def _swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr, low, high):
    _quick_sort(arr, low, high)

def _quick_sort(arr, low, high):
    if low + 64 > high: arr[low:high+1] = sorted(arr[low:high+1])
    else:
        _pivot(arr, low, high)
        i = _partition(arr, low, high)
        _quick_sort(arr, low, i-1)
        _quick_sort(arr, i+1, high)

def _pivot(arr, low, high):
    mid = (low + high) // 2
    if arr[low] > arr[mid]:
        _swap(arr, low, mid)
    if arr[low] > arr[high]:
        _swap(arr, low, high)
    if arr[mid] > arr[high]:
        _swap(arr, mid, high)

def _partition(arr, low, high):
    mid = (low + high) // 2
    pilot = arr[mid]
    _swap(arr, mid, high - 1)
    i = low
    j = high - 1
    while True:
        while True:
            i += 1
            if arr[i] >= pilot: break
        while True:
            j -= 1
            if arr[j] <= pilot: break
        if i >= j: break
        _swap(arr, i, j)
    _swap(arr, i, high - 1)
    return i

def generate_random_list(start, times):
    powerOfTwo = 2 ** times
    test_list = list(range(start*powerOfTwo))
    random.shuffle(test_list)
    return test_list, powerOfTwo

def tabulate_T_n(start, times):
    arr, powerOfTwo = generate_random_list(start, times)
    start_measure = time.time()
    quick_sort(arr, 0, len(arr)-1)
    end_measure = time.time()
    total_time = end_measure - start_measure
    return [(start*powerOfTwo, total_time)]

if __name__ == '__main__':
    final_results = []
    for i in range(10):
        result = tabulate_T_n(800, i)
        final_results.extend(result)
        print(result)
