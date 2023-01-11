class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self):
        self.head = None

    def create(self,value):
        newnode = Node(value)
        self.head = newnode

    def insertatbeg(self,value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode

    def insertatend(self,value):
        temp = self.head
        newnode = Node(value)
        if temp is None:
            temp=newnode
        else:
            while temp.next is not None:
                temp = temp.next
            newnode.prev = temp
            temp.next = newnode
            
    def deleteatbeg(self):
        if self.head is None:
            print("Empty")
        else:
            self.head = self.head.next

    def deleteatend(self):
        temp = self.head
        temp2 = None
        if self.head is None:
            print("Empty")
        else:
            while temp.next is not None:
                temp2 = temp
                temp = temp.next
            temp2.next = None

    def traversefront(self):
        temp = self.head
        if self.head is None:
            print("Empty")
        else:
            while temp.next is not None:
                print(temp.data)
                temp = temp.next
            print(temp.data)

    def traverseend(self):
        temp = self.head
        if self.head is None:
            print("Empty")
        else:
            while temp.next is not None:
                temp = temp.next
            while temp.prev is not None:
                print(temp.data)
                temp = temp.prev
            print(temp.data)

ll = LinkedList()
ll.create(20)
ll.insertatbeg(10)
ll.insertatend(30)
ll.insertatend(40)
ll.insertatend(50)
ll.insertatend(60)
ll.deleteatbeg()
ll.deleteatend()
ll.traversefront()
ll.traverseend()
ll.traversefront()
ll.traverseend()
