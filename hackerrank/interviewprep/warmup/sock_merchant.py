import math


def sock_merchant(n, ar):
    groups = {}
    for x in ar:
        groups[x] = groups[x] + 1 if x in groups else 1

    pairs = 0
    for group in groups:
        pairs += math.floor(groups[group] / 2)

    return pairs


if __name__ == '__main__':
    sock_merchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
