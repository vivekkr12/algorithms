def rot_left(a, d):
    la = len(a)
    b = [None] * la

    for i in range(la):
        b[i - d] = a[i]

    return b


if __name__ == '__main__':
    b_main = rot_left([1, 2, 3, 4, 5], 4)
    print(b_main)
