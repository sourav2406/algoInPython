#python3 programe for printing all permutation of given string

def toString(List):
    return ''.join(List)

def permute(arr, l, r):
    if l == r:
        print(toString(arr))
    else:
        for i in range(l, r + 1):
            arr[l], arr[i] = arr[i], arr[l]
            permute(arr, l + 1, r)
            arr[l], arr[i] = arr[i], arr[l]  #Backtrak
            
#driver code
if __name__ == "__main__":
    string = "ABC"
    n = len(string) 
    a = list(string) 
    permute(a, 0, n-1)