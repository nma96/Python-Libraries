from enum import Enum
from collections import OrderedDict


class State(Enum):
    unvisited = 1
    visited = 2
    visiting = 3


class Node(object):
    """docstring for Node"""

    def __init__(self, num):
        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()  # key = node, value = weight

    def __str__(self):
        return str(self.num)


class Graph(object):
    """docstring for Graph"""

    def __init__(self):
        self.nodes = OrderedDict()

    def add_node(self, num):
        tempNode = Node(num)
        self.nodes[num] = tempNode
        return tempNode

    def add_edge(self, source, dest, weight=0):
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[source].adjacent[self.nodes[dest]] = weight


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1, 5)
    print(g.nodes)
    g.add_edge(1, 2, 3)
    print(g.nodes)
