#python3 programe for bubble sort 

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if swapped == False:
            break

#driver code
if __name__ == "__main__":
    arr = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print(arr)
    bubbleSort(arr)
    print(arr)
            