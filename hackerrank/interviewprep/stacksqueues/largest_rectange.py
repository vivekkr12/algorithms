def largest_rectangle_brute_force(h):
    l_rect = 0
    n = len(h)
    for i in range(n):
        k = 1
        for left in reversed(range(0, i)):
            if h[left] >= h[i]:
                k += 1
            else:
                break
        for right in range(i + 1, n):
            if h[right] >= h[i]:
                k += 1
            else:
                break

        rect_area = k * h[i]
        if rect_area > l_rect:
            l_rect = rect_area

    return l_rect


if __name__ == '__main__':
    print(largest_rectangle_brute_force([1, 2, 3, 4, 5]))
    print(largest_rectangle_brute_force([8979, 4570, 6436, 5083, 7780, 3269, 5400, 7579, 2324, 2116]))
    print(largest_rectangle_brute_force([3, 3, 2, 1, 7, 6, 5]))
    print(largest_rectangle_brute_force([8, 4, 6, 5, 7, 3, 5, 7, 2, 2]))
