#python3 programe for selection sort

def sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]

if __name__ == "__main__":
    arr = [9, 8, 7, 6, 4, 3, 2, 1]
    print(arr)
    sort(arr)
    print(arr)
    