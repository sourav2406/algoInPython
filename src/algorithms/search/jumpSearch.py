import math

def search(arr, n, x):
    step = math.sqrt(n)

    step = int(min(step, n)-1)
    
    prev = 0
    while arr[step] < x:
        prev = step
        step += step
        
        if prev > n:
            return - 1
            
    while arr[int(prev)] < x:
        prev += 1
        if prev == min(step, n):
            return - 1
            
    if arr[int(prev)] == x:
        return prev

    return - 1
    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(search(arr, len(arr), 8))