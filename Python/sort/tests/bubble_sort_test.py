from sort.sources.bubbleSort import basic_bubble
from sort.sources.bubbleSort import recursive_bubble
arr = [64, 34, 25, 12, 22, 11, 90]
arr = basic_bubble(arr)
print("Basic Sorted array is: %s" % str(arr))

# Python 递归冒泡排序
arr = [64, 34, 25, 12, 22, 11, 90]
arr = recursive_bubble(arr)
print("Recursive Sorted array is: %s" % str(arr))

