import math


def binary_search(elements, e):
    return binary_search_inner(elements, e, 0)


def binary_search_inner(elements, e, index):
    if len(elements) == 1 and elements[0] is not e:
        return -1

    midpoint = math.floor(len(elements) / 2)
    if elements[midpoint] == e:
        return index + midpoint
    elif e < elements[midpoint]:
        return binary_search_inner(elements[:midpoint], e, index)
    else:
        return binary_search_inner(elements[midpoint:], e, index + midpoint)


if __name__ == '__main__':
    print(binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 23, 28, 101, 1001, 9999, 99999], 1001))
