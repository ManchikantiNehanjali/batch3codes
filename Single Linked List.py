class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def traverse(self):
        if self.head is None:
            print("LL is empty")
        else:
            n=self.head
            while(n!=None):
                print(n.data,end='->')
                n=n.ref
        
    def add(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=Node(data)
        
        if self.head==None:
            self.head=new_node
        else:
            n=self.head   
            while(n.ref!=None):
                n=n.ref
            n.ref=new_node
    def add_mid_aft(self,data,data1):
        new_node=Node(data)
        n=self.head
        while(n!=None and n.data!=data1):
            n=n.ref
        if n==None:
            print("Node not Found")
        else:
            t=n.ref
            n.ref=new_node
            new_node.ref=t
    def add_mid_bef(self,data,data1):
        new_node=Node(data)
        n=self.head
        if n.data==data1:
            self.head=new_node
            new_node.ref=n
        else:
            while(n.ref!=None and n.ref.data!=data1):
                n=n.ref
            if n.ref==None:
                print("Node not Found")
            else:
                t=n.ref
                n.ref=new_node
                new_node.ref=t
    def del_beg(self):
        if self.head is None:
            print("LL is Empty")
        else:
            self.head=self.head.ref
    def del_end(self):
        n=self.head
        if n is None:
            print("LL is empty")
        else:
            if n.ref is None:
                self.head=None
            else:
                while(n.ref.ref!=None):
                     n=n.ref
                n.ref=None
    
    def del_num(self,data):
        if self.head == None:
            print("LL is empty")
        else:
            if self.head.data==data:
                self.head=self.head.ref
            else:
                n=self.head
                while(n.ref !=None and n.ref.data!=data):
                    n=n.ref
                if n.ref==None:
                    print("Node not Found")
                else:
                    n.ref=n.ref.ref
                 
                
                    
ll=LinkedList()
ll.del_beg()
ll.del_end()
ll.del_num(1)
ll.add(7)
ll.add(4)
ll.add(6)
ll.add_end(10)
ll.add_mid_bef(17,4)
ll.add_mid_aft(34,6)
ll.add_mid_bef(19,100)
ll.add_mid_aft(45,69)
ll.traverse()
print()
ll.del_end()
ll.del_beg()
ll.del_num(123)
ll.del_num(4)
ll.traverse()
