import sys


def hourglass_sum(arr):
    # initialize to min value
    max_sum = -sys.maxsize - 1
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            sum_arr = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] \
                  + arr[i + 1][j + 1] \
                  + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]

        max_sum = sum_arr if sum_arr > max_sum else max_sum

    return max_sum


if __name__ == '__main__':
    max_sum_main = hourglass_sum([[1, 1, 1, 0, 0, 0],
                                  [0, 1, 0, 0, 0, 0],
                                  [1, 1, 1, 0, 0, 0],
                                  [0, 0, 2, 4, 4, 0],
                                  [0, 0, 0, 2, 0, 0],
                                  [0, 0, 1, 2, 4, 0]])

    print(max_sum_main)
