#python3 programe for printing level order of binary tree in spiral form
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
            
def printGivenLevel(node, level, ltr):
    if node is None:
        return
    if level == 1:
        print(node.data, end=' ')
    elif level > 1:
        if not ltr:
            printGivenLevel(node.left, level - 1, ltr)
            printGivenLevel(node.right, level - 1, ltr)
        else:
            printGivenLevel(node.right, level - 1, ltr)
            printGivenLevel(node.left, level - 1, ltr)
            
def printSpiral(node):
    h = height(node)
    ltr = False

    for i in range(1, h + 1):
        printGivenLevel(node, i, ltr)
        if i%2 == 0:
            ltr = not ltr
        print()

#driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)
root.left.left.left.left = Node(8)
root.left.left.left.right = Node(9)
printSpiral(root)