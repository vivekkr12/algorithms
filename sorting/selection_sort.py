def selection_sort(arr):
    """
    In a loop sets the ith element as unsorted and checks further down the array the smallest item. If found
    swaps the two elements.
    :param arr: original array of length n
    """
    n = len(arr)
    for i in range(n):
        smallest_index = i
        for j in range(i, n):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
            __swap__(arr, i, smallest_index)


def __swap__(arr, a, b):
    elem_a = arr[a]
    arr[a] = arr[b]
    arr[b] = elem_a


if __name__ == '__main__':
    array = [2, 3, 1, 10, 5, 6, 11, 25, 7, 6 ,3, 11, 22]
    print(array)
    selection_sort(array)
    print(array)
