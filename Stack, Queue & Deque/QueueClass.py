class Queue(object):
    """Visualize as Rear =========== Front"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        # Cannot use Append as we want to add to the front of the list so that we can pop the rear
        self.items.insert(0, item)

    def dequeue(self):
        # Cannot use self.items[0] because this only returns it but doesn't REMOVE it.
        return self.items.pop()

    def size(self):
        return len(self.items)
