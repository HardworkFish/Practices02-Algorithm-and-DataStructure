#!/usr/bin/env python
# Python 实现堆排序


# 维护最大堆
def heapify(arr, i, n):
    left, right = 2*i + 1, 2*i + 2
    lagest = i
    if i < n//2:
        if left < n and arr[left] > arr[lagest]:
            lagest = left
        if right < n and arr[right] > arr[lagest]:
            lagest = right
        if lagest != i:
            arr[lagest], arr[i] = arr[i], arr[lagest]
            heapify(arr, lagest, n)


# 构建最大堆
def build_max_heap(arr, n):
    for i in range(n//2, -1, -1):
        heapify(arr, i, n)


# 堆排序
def heap_sort(arr):
    build_max_heap(arr, len(arr))
    for i in range(len(arr)-1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)
    return arr



