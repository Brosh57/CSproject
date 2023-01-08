
class Node :
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    def create(self,val):
        newnode = Node(val)
        self.head = newnode

    def inatbeg(self,val):
        newnode = Node(val)
        if self.head is None:
            self.head = newnode
        else:       
            newnode.next = self.head
            self.head = newnode
        
    def inatend(self,val):
        newnode = Node(val)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode

    def deleteatbeg(self):
        if self.head is None:
            print("Empty")
        else:
            self.head=self.head.next
    
    def deleteatend(self):
        temp = self.head
        temp2 = 0
        if temp is None:
            print("Empty")
        else:
            while temp.next is not None:
                temp2=temp
                temp = temp.next
            temp2.next=None
            
    def traverse(self):
        temp = self.head
        while temp.next is not None :
            print(temp.data)
            temp = temp.next
        print(temp.data)

ll = LinkedList()
ll.create(20)
ll.inatbeg(30)
ll.inatend(45)
ll.inatend(3)
ll.traverse()
ll.deleteatbeg()
ll.deleteatend()
ll.traverse()