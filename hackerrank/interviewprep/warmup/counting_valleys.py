#!/bin/python3


# Complete the countingValleys function below.
def counting_valleys(n, s):
    level = 0
    valley = 0
    for i in range(n):
        level = level + 1 if s[i] == 'U' else level - 1
        if i != 0 and level == 0 and s[i] == 'U':
            valley += 1

    return valley


if __name__ == '__main__':
    v = counting_valleys(8, 'UDDDUDUU')
    print(v)
