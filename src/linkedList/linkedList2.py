class LinkedList:
    class Node:
        def __init__(self, newData):
            self.data = newData
            self.next = None
        
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data, end=' ') 
            temp = temp.next
        print("\n")

    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next

        print("\ncount : {}".format(count))

    def swapNode(self, x, y):
        if x == y:
            return

        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        if currX == None or currY == None:
            return
        print("hi")
        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY

        if prevY != None:
            prevY.next = currX
        else:
            self.head = currX

        temp = currX.next
        currX.next = currY.next
        currY.next = temp
        print("inside")

    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        self.head = prev
    
    def reverseInSize(self, head, k): 
        current = head  
        next  = None
        prev = None
        count = 0 
          
        # Reverse first k nodes of the linked list 
        while(current is not None and count < k): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next 
            count += 1
        # next is now a pointer to (k+1)th node 
        # recursively call for the list starting 
        # from current. And make rest of the list as 
        # next of first node 
        if next is not None: 
            head.next = self.reverseInSize(next, k) 
  
        # prev is new head of the input list 
        return prev 

if __name__ == "__main__":
    llist = LinkedList()
    llist.push(9) 
    llist.push(8) 
    llist.push(7) 
    llist.push(6) 
    llist.push(5) 
    llist.push(4) 
    llist.push(3) 
    llist.push(2) 
    llist.push(1)
    llist.printList()
    # llist.length()
    # llist.swapNode(3, 5)
    # llist.printList()
    # llist.reverse()
    # llist.printList()
    llist.head = llist.reverseInSize(llist.head,3)
    llist.printList()
    