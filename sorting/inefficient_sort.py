def inefficient_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        curr = arr[i]
        nxt = arr[i + 1]
        if curr > nxt:
            arr[i + 1] = curr
            arr[i] = nxt
            inefficient_sort(arr)


if __name__ == '__main__':
    array = [2, 3, 1, 10, 5, 6, 11, 25, 7, 6, 3, 11, 22]
    print(array)
    inefficient_sort(array)
    print(array)
