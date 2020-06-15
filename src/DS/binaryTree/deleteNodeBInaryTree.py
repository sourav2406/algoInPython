#Python3 programe for deleting node from binary tree

#Class for binary tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Print inorder of binary tree
def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)

#function for deleting deepest node in binary tree
def deepestDelete(root, d_node):
    queue = []
    queue.append(root)

    while (len(queue)):
        node = queue.pop(0)

        if node is d_node:
            node = None
            return

        if node.right:
            if node.right is d_node:
                node.right = None
                return
            else:
                queue.append(node.right)

        if node.left:
            if node.left is d_node:
                node.left = None
                return
            else:
                queue.append(node.left)

#Delete function for deleting node from binary tree
def delete(root, key):
    if root.left == None and root.right == None:
        if root.data == key:
            root.data = None
            return
        

    key_node = None
    queue = []
    queue.append(root)

    while (len(queue)):
        temp = queue.pop(0)

        if temp.data == key:
            key_node = temp
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

    if key_node:
        key_node.data = temp.data
        deepestDelete(root, temp)
        # temp = None
        # deleteDeepest(root, key_node)


#Driver code
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)

    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    print('Tree before deleting node.....')
    inorder(root)

    #delete key 12
    delete(root, 10)
    print('Tree after deleting 12 .....')
    inorder(root)