def jumping_on_clouds(c):
    c_len = len(c)
    steps = 0
    i = 0
    while i < c_len - 2:
        next_to_next = c[i + 2]
        i = i + 1 if next_to_next == 1 else i + 2
        steps += 1
        print(i, steps)

    steps = steps + 1 if (c_len - i - 1) != 0 else steps
    return steps


if __name__ == '__main__':
    x = jumping_on_clouds([0, 0, 1, 0, 0, 1, 0])
    print(x)
