class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class circular:
    def __init__(self):
        self.head=None
    def traverse(self):
        if self.head is None:
            print("CLL is empty")
            return
        n=self.head
        while True:
            print(n.data,end=">")
            n=n.next
            if n==self.head:
                print()
                break       
    def insertbeg(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
        else:
            n=self.head
            while(n.next!=self.head):
                n=n.next
            n.next=new_node
            new_node.next=self.head
            self.head=new_node
    def insertend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
        else:
            n=self.head
            while n.next!=self.head:
                n=n.next
            n.next=new_node
            new_node.next=self.head
    def insertbef(self,data,data1):
        if self.head is None:
            print("CLL is empty")
        else:
            new_node=Node(data)
            if self.head.data==data1:
                n=self.head
                while n.next!=self.head:
                    n=n.next
                n.next=new_node
                new_node.next=self.head
                self.head=new_node
            else:
                n=self.head
                while True:
                    if n.next==self.head or n.next.data==data1:
                        break
                    n=n.next
                if n.next==self.head:
                    print("Element not found")
                else:
                    t=n.next
                    n.next=new_node
                    new_node.next=t
    def insertaft(self,data,data1):
        if self.head is None:
            print("CLL is empty")
        else:
            n=self.head
            while True:
                if n.next==self.head or n.data==data1:
                    break
                n=n.next
            if n.data==data1:
                new_node=Node(data)
                new_node.next=n.next
                n.next=new_node
            else:
                print("Element not found")
    def delbeg(self):
        if self.head==None:
            print("CLL is empty")
        else:
            if self.head==self.head.next:
                self.head=None
                print("After deletion the CLL is empty")
            else:
                n=self.head
                while True:
                    if n.next==self.head:
                        n.next=self.head.next
                        self.head=self.head.next
                        break
                    n=n.next
    def delend(self):
        if self.head==None:
            print("CLL is empty")
        else:
            if self.head==self.head.next:
                self.head=None
                print("After deletion the CLL is empty")
            else:
                n=self.head
                while n.next.next != self.head:
                    n=n.next
                del n.next
                n.next=self.head
    def delbyval(self,data):
        if self.head is None:
            print("CLL is empty")
        else:
            if self.head.data==data and self.head==self.head.next:
                self.head=None
                print("After deletion the CLL is empty")
            else:
                if self.head.data==data:
                    n=self.head
                    while n.next!=self.head:
                        n=n.next
                    n.next=self.head.next
                    self.head=self.head.next
                else:
                    n=self.head
                    while n.next != self.head:
                        if n.next.data==data:
                            break
                        n=n.next
                    if n.next.data==data:
                        n.next=n.next.next
                    else:
                        print("Element not found")
                        
                        
                        
            
                
                
            
cll=circular()
