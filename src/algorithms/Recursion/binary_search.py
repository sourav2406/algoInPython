"""Binary Search using recursion"""


def binary_search(data, target, low, high):

    if low > high:
        return False
    else:
        mid = (low + high) // 2
        print(data[mid])
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


if __name__ == "__main__":
    data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("True" if binary_search(data1, 3, 0, 9) is True else "False")
