def minimum_bribes(q):
    array_len = len(q)
    bribes = 0

    for i in range(array_len):
        diff = q[i] - (i+1)
        if diff > 2:
            print('Too chaotic')
            return

        for j in range(max(0, q[i]-2), i):
            if q[j] > q[i]:
                bribes += 1

    print(bribes)


if __name__ == '__main__':
    minimum_bribes([1, 2, 5, 3, 4, 7, 8, 6])
