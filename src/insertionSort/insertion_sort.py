def insertion_sort(A):
    """Sort list elements in increasing order"""
    for k in range(1, len(A)):
        cur = A[k]
        j = k

        while j > 0 and A[j - 1] > cur:
            A[j] = A[j - 1]
            j -= 1
        A[j] = cur
    A.append(10)


if __name__ == "__main__":
    A = [5, 4, 3, 2, 1, 9, 8, 7, 6]
    insertion_sort(A)
    print(A)
