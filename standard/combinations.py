def get_combinations(arr, k):
    """
    Finds all the combinations of group size k from an array.\n
    The first set of groups would be incrementing just the last index, the second set of groups would increment the
    second last index and so on. Thus the groups would be\n
    (0, 1, ..., k - 1), (0 ,1, ..., k), (0 ,1, ..., k + 1), (0 ,1, ..., n-1),....., (n - k, n - k + 1, .... , n - 1)\n
    For example with n = 5 and k = 3, the groups would be:\n
    (0, 1, 2), (0, 1, 3), (0, 1, 4)\n
    (0, 2, 3), (0, 2, 4)\n
    (0, 3, 4)\n
    (1, 2, 3), (1, 2, 4)\n
    (1, 3, 4)\n
    (2, 3, 4)\n
    The algorithm is to find the last index that can be incremented, increase it and the fill the remaining items.\n
    :param arr: the original array of length n
    :param k: the size of each combination group
    :return: an array of all the combinations as tuples
    """
    combinations = []
    n = len(arr)

    if n < k:
        raise Exception("length of array is less than group size")
    if n == k:
        combinations.append(tuple(arr))
        return combinations

    group = list(range(0, k))
    combinations.append(__sublist_by_index__(arr, group))

    i = k - 1

    while i >= 0:

        while group[i] < n - k + i:
            group[i] = group[i] + 1
            for j in range(i + 1, k):
                group[j] = group[j - 1] + 1
            combinations.append(__sublist_by_index__(arr, group))
            # If something was filled to the right, reset i to k - 1
            if (i + 1) != k:
                i = k - 1

        i -= 1

    return combinations


def __sublist_by_index__(original_list, indexes):
    return tuple([original_list[i] for i in indexes])


if __name__ == '__main__':
    c = get_combinations([0, 1, 2, 3, 4, 5], 3)
    print(c)
    print(len(c))
