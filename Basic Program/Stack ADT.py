class Stack:
    def _init_(self):
        self.item = []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def is_empty(self):
        return len(self.item) == 0

S = Stack()
S.push(13)
S.push(25)
S.push(33)
print(S.pop())
print(S.peek())
print(S.is_empty())
