#!/usr/bin/env python
# Python 实现选择排序


def selection_sort(arr):
    n = len(arr)
    if n <= 1:
        return
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
