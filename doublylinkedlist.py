class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None

class doublyLL:
    def __init__(self):
        self.head=None
    def traverse(self):
        if self.head is None:
            print("LL is Empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=">")
                n=n.nref
            print()
    def reversell(self):
        if self.head is None:
            print("LL is Empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while(n !=None):
                print(n.data,end=">")
                n=n.pref
            print()
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("LL is not empty")
    def insert_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while(n.nref!=None):
                n=n.nref
            n.nref=new_node
            new_node.pref=n
    def insert_aft(self,data,data1):
        if self.head is None:
            print("LL is empty")
        else:
            n=self.head
            
            while(n is not None):
                if n.data!=data1:
                    n=n.nref
                else:
                    break
            if n is not None:
                new_node=Node(data)
                new_node.pref=n
                new_node.nref=n.nref
                if n.nref is not None:
                    n.nref.pref=new_node
                n.nref=new_node
            else:
                print("Node not found")
    def insert_bef(self,data,data1):
        if self.head is None:
            print("LL is empty")
        else:
            n=self.head
            while(n is not None):
                if n.data!=data1:
                    n=n.nref
                else:
                    break
            if n is not None:
                new_node=Node(data)
                new_node.pref=n.pref
                new_node.nref=n
                if n.pref is not None:
                    n.pref.nref=new_node
                else:
                    self.head=new_node#important
                n.pref=new_node
    def del_beg(self):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.nref==None:
            self.head.pref=None
            print("LL is empty after deleting the element")
        else:
            self.head=self.head.nref
            self.head.pref=None
            
    def del_end(self):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.nref==None:
            self.head=None
            print("LL is empty after deleting the element")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None
        
    def del_byval(self,data):
        if self.head is None:
            print("LL is empty")
            return
        
        if self.head.nref==None:
            if data==self.head.data:
                self.head=None
                print("LL is empty after deleting the element")
            else:
                print("Node not found")
            return
        
        if self.head.data==data:
            self.head=self.head.nref
            self.head.pref=None
            return
        n=self.head
        while n.nref!=None:
            if n.data==data:
                break
            else:
                n=n.nref
        if n.nref==None:
            if n.data==data:
                n.pref.nref=None
            else:
                print("Node not found")
        else:
            n.pref.nref=n.nref
            n.nref.pref=n.pref
            
                
            
dll=doublyLL()
