class Node(object):
    """docstring for Node"""

    def __init__(self, value):
        self.value = value
        self.nextnode = None
# -------------------------------------------------#
# Check if a cycle exists


def cycle_check(userNode):
    marker1 = userNode
    marker2 = userNode

    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        return marker1 == marker2

    return False
# -------------------------------------------------#

# Reverse the linked list


def reverse(head):

    current = head
    previous = None
    next_node = None

    while current:
        next_node = current.nextnode
        current.nextnode = previous
        previous = current
        current = next_node

    return previous

# -------------------------------------------------#

# Last but nth node finder.
# My Implementation


def nth_to_last_finder(n, head):

    totalNodes = 1
    current = head

    while current.nextnode:
        totalNodes += 1
        current = current.nextnode

    current = head
    required = totalNodes - n

    while required > 0:
        required -= 1
        current = current.nextnode

    return current

# Better Implementation
# Consider a horizontal node line. Have a box which is n nodes wide (with left edge and right edge)
# When right edge hits None, left edge will point at the required node.


def nth_to_last_node2(n, head):
    left_pointer = head
    right_pointer = head

    for i in range(n - 1):
        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list')

        right_pointer = right_pointer.nextnode

    # Until right_pointer reaches None
    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    return left_pointer


# a = Node(1)
# b = Node(2)
# c = Node(3)

# a.nextnode = b
# b.nextnode = c
# c.nextnode = a # Cycle Here!

# x = Node(1)
# y = Node(2)
# z = Node(3)

# x.nextnode = y
# y.nextnode = z

# cycle_check(a)
# cycle_check(x)

# reverse(a)
# reverse(x)

# target_node = nth_to_last_node(2, a)
# target_node.value
