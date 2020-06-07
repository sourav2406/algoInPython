from binarySearch import search

def exponentialSearch(arr, n, x):
    if arr[0] == x:
        return 0

    i = 1
    while i < n and arr[i] <= x:
        i *= 2

    return search(arr, int(i / 2), min(i, n), x)
    
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    print(exponentialSearch(arr, len(arr), 40))