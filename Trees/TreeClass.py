# Tree as nodes and references


class BinaryTree(object):

    def __init__(self, rootObj):
        self.rootObj = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):

        # If left child is empty, create a subtree at left child
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        # If left child isn't empty, push that child down and add new node to that place
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        # If right child is empty, create a subtree at right child
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        # If right child isn't empty, push that child down and add new node to that place
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootValue(self, obj):
        self.rootObj = obj

    def getRootValue(self):
        return self.rootObj

    def preorder(self):
        print(self.rootObj)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.rootObj)
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        if self.rightChild:
            self.rightChild.inorder()
        print(self.rootObj)


# r = BinaryTree('a')
# r.getRootValue()
# r.getRightChild()
# r.getLeftChild()

# r.insertLeft('b')
# r.getLeftChild().getRootValue()
