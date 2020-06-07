#python3 programe for recursive binary search

def search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return search(arr, 1, mid - 1, x)
        else:
            return search(arr, mid + 1, r, x)
    else:
        return - 1
        
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(search(arr, 0, len(arr) - 1, 7))
    
            