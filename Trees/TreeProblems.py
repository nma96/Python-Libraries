# Check if a Binary Tree is a Binary Search Tree
import collections


def inorder(tree):
    if tree is not None:
        inorder(tree.getLeftChild())
        tree_vals.append(tree.getRootVal())
        inorder(tree.getRightChild())


tree_vals = []


def sort_check(tree_vals):
    return tree_vals == sorted(tree_vals)


inorder(tree)
sort_check(tree_vals)


# keep track of the minimum and maximum values a node can take

class Node:
    def __init__(self, k, val):
        self.key = k
        self.value = val
        self.left = None
        self.right = None


def tree_max(node):
    if not node:
        return float("-inf")
    maxleft = tree_max(node.left)
    maxright = tree_max(node.right)
    return max(node.key, maxleft, maxright)


def tree_min(node):
    if not node:
        return float("inf")
    minleft = tree_min(node.left)
    minright = tree_min(node.right)
    return min(node.key, minleft, minright)


def verify(node):
    if not node:
        return True
    if (tree_max(node.left) <= node.key <= tree_min(node.right) and
            verify(node.left) and verify(node.right)):
        return True
    else:
        return False


root = Node(10, "Hello")
root.left = Node(5, "Five")
root.right = Node(30, "Thirty")

print(verify(root))  # prints True, since this tree is valid

root = Node(10, "Ten")
root.right = Node(20, "Twenty")
root.left = Node(5, "Five")
root.left.right = Node(15, "Fifteen")

print(verify(root))  # prints False, since 15 is to the left of 10


# -------------------------------------------------#


# Tree Level Order Print


class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


def levelOrderPrint(tree):
    if not tree:
        return
    nodes = collections.deque([tree])
    currentCount, nextCount = 1, 0
    while len(nodes) != 0:
        currentNode = nodes.popleft()
        currentCount -= 1
        print currentNode.val,
        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount += 1
        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount += 1
        if currentCount == 0:
            # finished printing current level
            print '\n',
            currentCount, nextCount = nextCount, currentCount

# root = Node(1)

# root.left = Node(2)
# root.right = Node(3)
# levelOrderPrint(root)


# -------------------------------------------------#

# Trim a binary search tree

def trimBST(tree, minVal, maxVal):

    if not tree:
        return

    tree.left = trimBST(tree.left, minVal, maxVal)  # Postorder traversal
    tree.right = trimBST(tree.right, minVal, maxVal)

    if minVal <= tree.val <= maxVal:
        return tree

    # Return only the right subtree because the left subtree is smaller than the minVal
    if tree.val < minVal:
        return tree.right

    # Return only the left subtree because the right subtree is bigger than the maxVal
    if tree.val > maxVal:
        return tree.left
