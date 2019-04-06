def match(input_string):
    char_stack = []
    index_stack = []

    result = ['x'] * len(input_string)

    for i, e in enumerate(input_string):
        if e is '(':
            char_stack.append(e)
            index_stack.append(i)
        elif e is ')':
            if char_stack and char_stack[-1] is '(':
                result[index_stack.pop()] = '0'
                result[i] = '0'
                char_stack.pop()
            else:
                char_stack.append(e)
                index_stack.append(i)
        else:
            result[i] = e

    while char_stack:
        x = char_stack.pop()
        if x == '(':
            result[index_stack.pop()] = '1'
        elif x == ')':
            result[index_stack.pop()] = '-1'

    return ''.join(result)


if __name__ == '__main__':
    print(match("()"), " | Expected: 00")
    print(match(")("), " | Expected: -11")
    print(match("(a)"), " | Expected: 0a0")
    print(match("((a))"), " | Expected: 00a00")
    print(match("((a)"), " | Expected: 10a0")
    print(match(")(alfredo)"), " | Expected: -10alfredo0")
    print(match(")(alfredo)("), " | Expected: -10alfredo0")
