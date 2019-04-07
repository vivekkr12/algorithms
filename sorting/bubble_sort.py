def bubble_sort(arr):
    """
    Sorts the array by checking the adjacent pairs. Using this algorithm, the elements at the end
    are sorted first. Loop though the array n times and check if any of the pairs need swapping. If
    there was no swap, then the array was sorted
    :param arr: original array of length n
    """
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                __swap__(arr, i, i + 1)
                swapped = True


def __swap__(arr, a, b):
    elem_a = arr[a]
    arr[a] = arr[b]
    arr[b] = elem_a


if __name__ == '__main__':
    array = [2, 3, 1, 10, 5, 6, 11, 25, 7, 6 ,3, 11, 22]
    print(array)
    bubble_sort(array)
    print(array)
