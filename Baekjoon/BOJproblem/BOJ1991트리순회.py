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

if __name__ == "__main__":
    N = int(input())
    arr = []
    for i in range(N):
        #print(chr(65 + i))
        arr.append(Node(chr(65 + i)))

    tree = Tree()
    #tree.root = tree[0]
    for i in range(N):
        L = input().split()
        if L[1] != '.':
            arr[ord(L[0]) - 65].left = arr[ord(L[1]) - 65]
        if L[2] != '.':
            arr[ord(L[0]) - 65].right = arr[ord(L[2]) - 65]


    tree.preorder(arr[0])
    print()
    tree.inorder(arr[0])
    print()
    tree.postorder(arr[0])