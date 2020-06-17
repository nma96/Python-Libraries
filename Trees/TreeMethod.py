# Implemented as List of Lists (Udemy Videoo 108)


def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop()

    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])

    return root


def insertRight(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])

    return root


def getRootValue(root):
    return root[0]


def setRootValue(root, newValue):
    root[0] = newValue


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]
