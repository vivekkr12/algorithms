def count_swaps(a):
    n = len(a)
    swapped = True
    swap_count = 0
    while swapped:
        swapped = False
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                __swap__(a, i, i + 1)
                swapped = True
                swap_count += 1

    print('Array is sorted in {} swaps.'.format(swap_count))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[n - 1]))


def __swap__(arr, a, b):
    if a == b:
        return
    elem_a = arr[a]
    arr[a] = arr[b]
    arr[b] = elem_a


if __name__ == '__main__':
    count_swaps([3, 2, 1])
    count_swaps([1, 2, 3])

