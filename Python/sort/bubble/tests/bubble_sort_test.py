import sys
import time
sys.path.append('../sources/')
from sort.bubble.sources.bubbleSort import basic_bubble
from sort.bubble.sources.bubbleSort import recursive_bubble
arr = [64,34,25,12,22,11,90]
start = time.time()
arr = basic_bubble(arr)
end = time.time()
print("Basic Sorted array is: %s" % str(arr))

##### Python 递归冒泡排序 #######
arr = [64,34,25,12,22,11,90]
start = time.time()
arr = recursive_bubble(arr)
end = time.time()
print("Recursive Sorted array is: %s" % str(arr))

