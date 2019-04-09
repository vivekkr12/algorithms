def is_balanced(s):
    stack = []
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        elif c == ')' or c == '}' or c == ']':

            if len(stack) == 0:
                return 'NO'

            popped = stack.pop()
            if popped == '(' and c != ')':
                return 'NO'
            if popped == '{' and c != '}':
                return 'NO'
            if popped == '[' and c != ']':
                return 'NO'

    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    print(is_balanced('{[()]}'))
    print(is_balanced('{[(])}'))
    print(is_balanced('{{[[(())]]}}'))
    print(is_balanced('{{([])}}'))
    print(is_balanced('{{)[](}}'))
    print(is_balanced('{(([])[])[]}'))
    print(is_balanced('{(([])[])[]]}'))
    print(is_balanced('{(([])[])[]}[]'))

    print(is_balanced('}][}}(}][))]'))
    print(is_balanced('[](){()}'))
    print(is_balanced('()'))
    print(is_balanced('({}([][]))[]()'))
    print(is_balanced('{)[](}]}]}))}(())('))
    print(is_balanced('([[)'))
