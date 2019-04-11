class Editor:

    def __init__(self):
        self.s = ''
        self.op_history = []

    def append(self, w):
        wn = len(w)
        self.op_history.append((1, wn))
        self.s += w

    def delete(self, k):
        deleted = self.s[-k:]
        self.s = self.s[:-k]
        self.op_history.append((2, deleted))

    def print(self, k):
        print(self.s[k - 1])

    def undo(self):
        op = self.op_history.pop()
        if op[0] == 1:
            k = op[1]
            self.s = self.s[:-k]
        elif op[0] == 2:
            self.s += op[1]


if __name__ == '__main__':
    editor = Editor()
    num_input = int(input())
    for i in range(num_input):
        input_line = input().split()
        if input_line[0] == '1':
            editor.append(input_line[1])
        elif input_line[0] == '2':
            editor.delete(int(input_line[1]))
        elif input_line[0] == '3':
            editor.print(int(input_line[1]))
        elif input_line[0] == '4':
            editor.undo()
