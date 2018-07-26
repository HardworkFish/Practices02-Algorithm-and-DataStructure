#!/usr/bin/env python
# Python 实现插入排序
def basic_insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key <arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr

def recursive_insertion(arr,n):
    # base case
    if n <=1:
        return
    # 对 n-1 个元素进行递归排序
    recursive_insertion(arr,n-1)
    # 将最后一个元素插入到已排序序列对应位置
    last = arr[n-1]
    j = n-2
    # 移动比 key大的 arr[0...i-1] 中的元素到后一个位置

    while(j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = last

    return arr
