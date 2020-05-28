def search(arr, element):
    for index, eachElement in enumerate(arr):
        if eachElement == element:
            return index
    
    return - 1
    
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(search(arr, 21))