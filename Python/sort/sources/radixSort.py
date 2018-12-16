#!/usr/bin/env python
# Python 实现基数排序


def countingSort(arr, exp1):
    n = len(arr)

    # 存储输出数组
    output = [0] * (n)

    # 初始化计数数组
    count = [0] * (10)

    # 存储当前计数值
    for i in range(0, n):
        index = (arr[i] // exp1)
        count[(index) % 10] += 1

    #  计数
    for i in range(1, 10):
        count[i] += count[i - 1]

        # 构造输出数组
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp1)
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1
        i -= 1

    # 将输出数组复制到 arr
    # arr 已为排序好的数组
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    # max1 为数组中的最大数
    max1 = max(arr)

    # 对每个元素进行计数排序，不是传递数字而是传递 exp，exp 是 10^, i 为当前数字
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10
    return  arr