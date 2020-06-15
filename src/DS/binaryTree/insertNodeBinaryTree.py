#Python3 programe for inserting value in inorder binary tree

#Class for binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Class for binary tree
class BinaryTree:
    def __init__(self, root):
        self.root = root

    #function for inorder traversal of tree
    def inorderTrversal(self, node):
        if not node:
            return 0

        self.inorderTrversal(node.left)
        print(node.data, end=" ")
        self.inorderTrversal(node.right)

    #Function for inserting data into tree
    def insert(self, data):
        queue = []
        queue.append(self.root)

        while (len(queue)):
            node = queue[0]
            queue.pop(0)

            if not node.left:
                node.left = Node(data)
                break
            else:
                queue.append(node.left)

            if not node.right:
                node.right = Node(data)
                break
            else:
                queue.append(node.right)

#Driver code
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)

    root.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)

    binaryTree = BinaryTree(root)
    
    print("Printing inorder traversal before inserting.....")
    binaryTree.inorderTrversal(binaryTree.root)

    binaryTree.insert(7)
    
    print()
    print("Printing inorder traversal after inserting data.....")
    binaryTree.inorderTrversal(binaryTree.root)