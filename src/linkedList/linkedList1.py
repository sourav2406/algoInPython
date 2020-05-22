class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, newData):
        new_node = Node(newData)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, previousNode, newData):
        if previousNode is None:
            print('The given previous node should be valid.')
            return

        new_node = Node(newData)

        new_node.next = previousNode.next
        previousNode.next = new_node

    def append(self, newData):
        new_node = Node(newData)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node

    def deleteNode(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        
        while temp:
            if temp.data == key:
                break
            prv = temp
            temp = temp.next
        
        if temp is None:
            return

        prv.next = temp.next
        temp = None

# Code execution starts here
if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third
    llist.push(4)
    llist.push(5)
    llist.append(20)
    llist.insertAfter(llist.head.next, 27)
    llist.append(21)

    llist.deleteNode(3)

    llist.printList()