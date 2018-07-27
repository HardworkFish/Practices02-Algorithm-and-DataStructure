from sort.sources.quickSort import quickSort
arr = [64,34,25,12,22,11,90]
n = len(arr)
arr = quickSort(arr, 0, n-1)
print('Quick Sort: %s' % arr)