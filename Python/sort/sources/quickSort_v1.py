#!/usr/bin/env python
# Python 实现快排(降序)


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] > pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_v1(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_v1(arr, low, pi-1)
        quick_sort_v1(arr, pi+1, high)
    return arr


