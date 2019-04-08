import math


def pairs(k, arr):
    arr.sort()
    n = len(arr)
    count_pairs = 0
    for i in range(n):
        if binary_search(arr, arr[i] + k):
            count_pairs += 1

    return count_pairs


def binary_search(arr, x):
    n = len(arr)
    if n == 0:
        return False
    i = math.floor(n / 2)
    if x == arr[i]:
        return True
    elif x > arr[i]:
        return binary_search(arr[i + 1:n], x)
    else:
        return binary_search(arr[0:i], x)


def pairs_two_pointers(k, arr):
    i = 0
    j = 1
    count_pairs = 0
    arr.sort()
    n = len(arr)
    while j < n:
        diff = arr[j] - arr[i]
        if diff == k:
            count_pairs += 1
            j += 1
        elif diff < k:
            j += 1
        elif diff > k:
            i += 1
    return count_pairs


if __name__ == '__main__':
    count = pairs_two_pointers(2, [1, 5, 3, 4, 2])
    print(count)
