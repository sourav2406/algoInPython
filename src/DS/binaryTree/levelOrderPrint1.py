#Python3 programe for printing level order of binary tree using recursion

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

def printGivenLevel(node, level):
    if node is None:
        return
    if level == 1:
        print(node.data, end=' ')
    elif level > 1:
        printGivenLevel(node.left, level - 1)
        printGivenLevel(node.right, level - 1)
        
def printLevelOrder(node):
    h = height(node)
    for i in range(1, h + 1):
        printGivenLevel(node, i)
        print()

#Driver code
if __name__ == "__main__":
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    
    print("Level order traversal of binary tree is -") 
    printLevelOrder(root)
    