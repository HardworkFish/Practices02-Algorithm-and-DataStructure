#!/usr/bin/env python
# Python 实现归并排序


def merge(left, right):
    """
    比较传过来的两个序列 left, right, 返回一个排好的序列
    :param left:
    :param right:
    :return:
    """
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(arr):
    """
    归并排序算法 Python 算法
    :param arr:
    :return:
    """
    if len(arr) <= 1:  # 将序列不断分为小切片
        return arr
    mid = int(len(arr)/2)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # 第一次传过去的是[left=5, right=4], 第二次传过去的是 [left=7, right=4, 5]
    return merge(left, right)




