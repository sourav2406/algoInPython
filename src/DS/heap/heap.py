def left(i):
    return (2 * i) + 1
    
def right(i):
    return (2 * i) + 2
    
def parent(i):
    return (i-1) // 2
    
def max_heapify(arr, i, size=None):
    l = left(i)
    r = right(i)
    heapSize = size if size != None else len(arr) - 1

    if l <= heapSize and arr[l] > arr[i]:
        largest = l
    else:
        largest = i

    if r <= heapSize and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heapSize)

def build_heap(arr,size=None):
    heapSize = size if size != None else len(arr) - 1
    p = parent(heapSize)
    for i in range(p, -1, -1):
        max_heapify(arr, i, heapSize)

def heap_sort(arr):
    build_heap(arr)
    print(arr)
    heapSize = len(arr) - 1
    arr[heapSize], arr[0] = arr[0], arr[heapSize]
    
    for i in range(heapSize - 1, 0, -1):
        max_heapify(arr, 0, i)
        # build_heap(arr, i)
        arr[i], arr[0] = arr[0], arr[i]
        


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr1 = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    arr2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    # print(arr)
    # print(parent(len(arr)-1))
    # max_heapify(arr, 0)
    # build_heap(arr)
    heap_sort(arr1)
    heap_sort(arr2)
    print(arr2)