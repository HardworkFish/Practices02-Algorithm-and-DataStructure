#!/usr/bin/env python
# Python 实现希尔排序


def shell_sort(arr):
    n = len(arr)
    gap = int(n/2)  # 初始化 gap 值
    # 第一层循环：依次改变 gap 值对列表进行分组
    # 下面：利用直接插入排序的思想对分组元素进行排序
    # range(gap, n) 从 gap 开始
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # 类似插入排序, 当前值与指定步长之前的值比较, 符合条件则交换位置
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        # while 循环条件折半
        gap = int(gap/2)
    return arr



