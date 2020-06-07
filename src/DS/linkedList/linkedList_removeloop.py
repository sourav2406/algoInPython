class LinkedList():
    class Node():
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def push(self, data):
        node = self.Node(data)
        node.next = self.head
        self.head = node

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def detectAndRemoveLoop(self):
        slow_p = fast_p = self.head
        while (slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if slow_p == fast_p:
                self.removeLoop(slow_p)
                return True
        
        return False

    def removeLoop(self, loopNode):
        ptr1 = self.head

        while (1):
            ptr2 = loopNode
            while (ptr2.next != loopNode and ptr2.next != ptr1):
                ptr2 = ptr2.next
            
            if ptr2.next == ptr1:
                break

            ptr1 = ptr1.next

        ptr2.next = None

if __name__ == "__main__":
    llist = LinkedList()
    llist.push(10)
    llist.push(4)
    llist.push(15)
    llist.push(20)
    llist.push(50)

    llist.head.next.next.next.next.next = llist.head.next.next
    llist.detectAndRemoveLoop()
    llist.printLinkedList()

        