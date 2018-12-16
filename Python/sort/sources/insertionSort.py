#!/usr/bin/env python
# Python 实现插入排序

# 直接插入排序
"""
时间复杂度：O(n**2)
空间复杂度：O（1）
稳定性：稳定
思想：先将前两个元素排序，将第三个元素插入前面已经排好序的序列，后面的元素依次插入前面已经排好的序列。

"""


def basic_insertion(arr):
    n = len(arr)
    if n <= 1:
        return
    for i in range(1, len(arr)):
        # key（本轮所选择的元素） 指向尚未排序好的元素(从第二个开始)
        key = arr[i]
        # j 指向下一个元素下标
        j = i-1
        # key 与前一个元素比较，若 key 较小，则前一个元素后移，j自减，继续比较
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        # key 指向元素的最终位置
        arr[j+1] = key
    return arr


# 递归插入排序
def recursive_insertion(arr, n):
    # base case
    if n <=1:
        return
    # 对 n-1 个元素进行递归排序
    recursive_insertion(arr, n-1)
    # 将最后一个元素插入到已排序序列对应位置
    last = arr[n-1]
    j = n-2
    # 移动比 key大的 arr[0...i-1] 中的元素到后一个位置
    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j = j-1
    arr[j+1] = last
    return arr
