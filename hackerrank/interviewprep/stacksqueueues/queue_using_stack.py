class MyQueue(object):
    def __init__(self):
        self.stack_put = []
        self.stack_pop = []

    def peek(self):
        if self.stack_pop:
            return self.stack_pop[-1]
        self.__fill_stack_pop__()
        return self.stack_pop[-1]

    def pop(self):
        if self.stack_pop:
            return self.stack_pop.pop()
        self.__fill_stack_pop__()
        return self.stack_pop.pop()

    def put(self, value):
        self.stack_put.append(value)

    def __fill_stack_pop__(self):
        while self.stack_put:
            self.stack_pop.append(self.stack_put.pop())


if __name__ == '__main__':
    queue = MyQueue()
    query_list = ['1 42', '2', '1 14', '3', '1 28', '3', '1 60', '1 78', '2', '2']
    for line in query_list:
        values = map(int, line.split())
        values = list(values)
        if values[0] == 1:
            queue.put(values[1])
        elif values[0] == 2:
            queue.pop()
        else:
            print(queue.peek())

