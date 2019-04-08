def quick_sort(arr):
    """
    Algorithm: At first choose the first element as the pivot. In the partition method, the pivot must
    go to its correct place (the one in final sorted array).\n
    For the partition method, mark the first element as the pivot. The second element as storage index.
    For i in pivot + 1 to hi, check if arr[i] < arr[pivot]. If yes, swap it with storage index and increment
    storage index by 1. Once the loop ends, swap pivot with storage index - 1. Return the new pivot index i.e
    storage index - 1
    :param arr: original array of length n
    """
    n = len(arr)
    __sort__(arr, 0, n - 1)


def __sort__(arr, lo, hi):
    if lo >= hi:
        return
    pivot = __partition__(arr, lo, hi)
    print(arr[lo: pivot], arr[pivot], arr[pivot + 1: hi + 1])
    __sort__(arr, lo, pivot - 1)
    __sort__(arr, pivot + 1, hi)


def __partition__(arr, lo, hi):
    pivot = lo
    storage_index = pivot + 1
    for i in range(pivot + 1, hi + 1):
        if arr[i] < arr[pivot]:
            __swap__(arr, i, storage_index)
            storage_index += 1
    __swap__(arr, pivot, storage_index - 1)
    return storage_index - 1


def __swap__(arr, a, b):
    if a == b:
        return
    elem_a = arr[a]
    arr[a] = arr[b]
    arr[b] = elem_a


if __name__ == '__main__':
    array = [13, 30, 2, 3, 1, 10, 5, 6, 11, 25, 7, 6 ,3, 11, 22]
    print(array)
    quick_sort(array)
    print(array)
