def repeated_string(s, n):
    s_len = len(s)
    count_a = 0

    for c in s:
        if c == 'a':
            count_a += 1

    total_count_a = count_a * int(n / s_len)

    left = n % s_len
    for c in s[0:left]:
        if c == 'a':
            total_count_a += 1

    return total_count_a


if __name__ == '__main__':
    pass
