from sort.sources.quickSort import quick_sort
from sort.sources.quickSort_v1 import quick_sort_v1
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
# Python 快排(升序)
arr = quick_sort(arr, 0, n-1)
print('Quick Sort: %s' % arr)
# Python 快排(降序)
arr = quick_sort_v1(arr, 0, n-1)
print("Quick Sort: %s" % arr)


