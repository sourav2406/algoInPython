#python3 programe for insertion sort

def insertionSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

#driver code
if __name__ == "__main__":
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(arr)
    insertionSort(arr)
    print(arr)
    