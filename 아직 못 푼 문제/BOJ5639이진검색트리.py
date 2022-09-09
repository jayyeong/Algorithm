import heapq

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def preorder(self,n):
        if n != None:
            print(n.data,end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self,n):
        if n != None:

            if n.left:
                self.inorder(n.left)
            print(n.data, end='')
            if n.right:
                self.inorder(n.right)

    def postorder(self,n):
        if n != None:

            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(n.data, end='')