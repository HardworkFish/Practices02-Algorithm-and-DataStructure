#!/usr/bin/env python
# Python 程序完成冒泡排序


# 一般冒泡
def basic_bubble(arr):
    n = len(arr)
    if n <= 1:
        return

    for i in range(n):  # 遍历所有数组元素
        # 已经到了最后一个元素位置
        for j in range(0, n-i-1):
            # 从[0,n-i-1]遍历数组
            # 如果找到的元素更大，则交换
            # 继续比较下一个元素
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# 递归实现冒泡排序
def recursive_bubble(arr):
    for i, num in enumerate(arr):
        try:
            if arr[i+1] < num:
                arr[i] = arr[i+1]
                arr[i+1] = num
                recursive_bubble(arr)
        except IndexError:
            pass
    return arr
