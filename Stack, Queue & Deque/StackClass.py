class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        # -1 Because indexing starts at 0
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
