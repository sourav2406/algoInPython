class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    current = root
    stack = []

    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif (stack):
            current = stack.pop()
            print(current.data, end=' ')
            current = current.right
        else:
            break

    print()

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    inorder(root)