class Node(object):
    """docstring for node"""

    def __init__(self, value):

        self.value = value
        self.next_node = None
        self.prev_node = None

# a = Node(1)
# b = Node(2)
# c = Node(3)

# Setting b after a
# b.prev_node = a
# a.next_node = b

# Setting c after a
# b.next_node = c
# c.prev_node = b
