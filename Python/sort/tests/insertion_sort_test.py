from sort.sources.insertionSort import basic_insertion
from sort.sources.insertionSort import recursive_insertion
arr = [64, 34, 25, 12, 22, 11, 90]
arr = basic_insertion(arr)
print("Basic Insertion Sort: %s" % str(arr))


# 递归插入排序
arr = [64, 34, 25, 12, 22, 11, 90]
arr = recursive_insertion(arr,7)
print("Recursive Insertion Sort: %s" % str(arr))
